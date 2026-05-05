import os
import requests
import pytest
from dotenv import load_dotenv
import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

# 配置日志（输出到控制台和文件）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('test_run.log', encoding='utf-8'),
        logging.StreamHandler()
    ],
    force=True
)
# 让 tenacity 输出重试日志
logging.getLogger("tenacity").setLevel(logging.INFO)

# 加载 .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("PASSWORD")

# 登录函数（带重试）
@retry(stop=stop_after_attempt(3),       # 最多尝试3次
       wait=wait_fixed(1),               # 每次重试间隔1秒
       retry=retry_if_exception_type(requests.exceptions.HTTPError))
def login():
    logging.info("开始调用登录接口")
    url = f"{BASE_URL}/post"
    payload = {"username": USERNAME, "password": PASSWORD}
    resp = requests.post(url, json=payload,  )
    resp.raise_for_status()   # 如果状态码不是2xx，抛出 HTTPError
    data = resp.json()
    returned_username = data["json"]["username"]
    token = returned_username + "_token"
    logging.info(f"登录成功，获得 token: {token}")
    return token

@pytest.fixture(scope="session")
def auth_token():
    logging.info("执行 fixture，获取 token（整个会话一次）")
    token = login()
    return token

def test_bearer_check(auth_token):
    logging.info("测试1：验证 /bearer 端点")
    headers = {"Authorization": f"Bearer {auth_token}"}
    url = f"{BASE_URL}/bearer"
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["token"] == auth_token
    logging.info("测试1通过")

def test_anything_check(auth_token):
    logging.info("测试2：验证 /anything 端点中的 Authorization 头")
    headers = {"Authorization": f"Bearer {auth_token}"}
    url = f"{BASE_URL}/anything"
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["headers"].get("Authorization") == f"Bearer {auth_token}"
    logging.info("测试2通过")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=report.html", "--self-contained-html"])