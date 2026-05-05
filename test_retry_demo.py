# import requests
# import logging
#
# # 配置日志（简单版本）
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def unstable_request():
#     """模拟一个偶尔失败的请求"""
#     # 这里故意请求一个会返回 500 错误的地址（httpbin 提供）
#     url = "https://httpbin.org/status/500"
#     resp = requests.get(url)
#     resp.raise_for_status()   # 如果状态码不是 200，会抛出 HTTPError
#     return resp.json()
#
# def test_without_retry():
#     logging.info("开始请求")
#     data = unstable_request()  # 这里会直接抛出异常，测试失败
#     logging.info("请求成功")




import requests
import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def unstable_request():
    """模拟一个偶尔失败的请求（总是返回500）"""
    url = "https://httpbin.org/status/500"
    resp = requests.get(url)
    resp.raise_for_status()   # 抛出 HTTPError
    return resp.json()

@retry(stop=stop_after_attempt(3),       # 最多重试3次
       wait=wait_fixed(1),               # 每次重试间隔1秒
       retry=retry_if_exception_type(requests.exceptions.HTTPError))  # 仅对 HTTPError 重试
def stable_request():
    url = "https://httpbin.org/status/500"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def test_without_retry():
    logging.info("开始请求（无重试）")
    data = unstable_request()
    logging.info("请求成功")

def test_with_retry():
    logging.info("开始请求（带重试）")
    data = stable_request()
    logging.info("请求成功")