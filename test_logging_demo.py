import logging
import time

# 配置 logging（放在文件顶部，所有导入之后）
logging.basicConfig(
    level=logging.INFO,  # 输出 INFO 级别及以上的日志
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('test_run.log', encoding='utf-8'),  # 输出到文件
        logging.StreamHandler()  # 同时输出到控制台
    ],
    force=True   # 加上这一行
)

def fake_login():
    logging.info("开始调用登录接口")
    # 模拟请求
    time.sleep(0.5)
    logging.info("登录成功，返回 token")
    return "fake_token"

def test_something():
    logging.info("测试开始")
    token = fake_login()
    logging.info(f"获取到的 token: {token}")
    assert token is not None
    logging.info("断言通过，测试结束")

if __name__ == "__main__":
    test_something()

# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# logging.info("测试开始")
# logging.error("出错了")