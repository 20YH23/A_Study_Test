# import requests
# import pytest
#
# # 登录函数：发送账号密码，返回 token
# def login():
#     url = "https://reqres.in/api/login"
#     # 这个测试账号密码是官方提供的
#     payload = {
#         "email": "eve.holt@reqres.in",
#         "password": "cityslicka"
#     }
#     resp = requests.post(url, json=payload)
#     # 登录成功应该返回 200
#     assert resp.status_code == 200
#     # 从响应中提取 token 字段
#     token = resp.json()["token"]
#     return token
#
# # 测试1：直接验证登录能拿到 token
# def test_login():
#     token = login()
#     assert token is not None
#     assert isinstance(token, str)
#     print(f"获取到的 token: {token}")
#
# # 测试2：使用 token 访问需要认证的接口（获取用户信息）
# def test_get_user_with_token():
#     token = login()   # 先登录
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     url = "https://reqres.in/api/users/2"
#     resp = requests.get(url, headers=headers)
#     assert resp.status_code == 200
#     data = resp.json()
#     assert data["data"]["id"] == 2
#     assert data["data"]["email"] == "janet.weaver@reqres.in"



# import requests
# import pytest
#
# def login():
#     url = "https://httpbin.org/post"
#     payload = {"username": "test", "password": "123"}
#     resp = requests.post(url, json=payload)
#     # httpbin 总是返回 200，我们从响应中构造一个 token（实际项目中是 resp.json()["token"]）
#     assert resp.status_code == 200
#     # 模拟 token：这里用响应中的一些数据拼凑，实际上你可以直接写固定值
#     token = resp.json()["json"]["username"] + "_token"   # 得到 "test_token"
#     return token
#
# def test_get_user_with_token():
#     token = login()
#     headers = {"Authorization": f"Bearer {token}"}
#     # 现在用这个 token 去请求需要认证的资源（这里仍用 httpbin 的 /bearer 演示）
#     resp = requests.get("https://httpbin.org/bearer", headers=headers)
#     assert resp.status_code == 200
#     assert resp.json()["token"] == token


# import pytest
# import requests
#
# # 登录函数保持不变
# def login():
#     url = "https://httpbin.org/post"
#     payload = {"username": "test", "password": "123"}
#     resp = requests.post(url, json=payload)
#     assert resp.status_code == 200
#     token = resp.json()["json"]["username"] + "_token"
#     return token
#
# # 这是一个 fixture，名字叫 auth_token
# @pytest.fixture
# def auth_token():
#     token = login()
#     return token
#
# # 测试函数直接使用 fixture 作为参数，pytest 会自动把返回值传进来
# def test_get_user_with_token(auth_token):
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     resp = requests.get("http s://httpbin.org/bearer", headers=headers)
#     assert resp.status_code == 200
#     assert resp.json()["token"] == auth_token



# import pytest
# import requests
#
# def login():
#     url = "https://httpbin.org/post"
#     payload = {"username": "test", "password": "123"}
#     resp = requests.post(url, json=payload)
#     assert resp.status_code == 200
#     token = resp.json()["json"]["username"] + "_token"
#     return token
#
# @pytest.fixture(scope="session")
# def auth_token():
#     print("\n>>> 登录一次，获取 token（整个会话只执行一次）")
#     token = login()
#     return token
#
# def test_api_1(auth_token):
#     print(f"\n测试1 使用的 token: {auth_token}")
#     # 这里写具体的接口测试逻辑
#     assert True
#
# def test_api_2(auth_token):
#     print(f"\n测试2 使用的 token: {auth_token}")
#     assert True

# import pytest
# import requests
# import os
# from dotenv import load_dotenv
#
# # 加载 .env 文件中的环境变量
# load_dotenv()
#
#
# def login():
#     # 从环境变量中读取配置，省去硬编码
#     base_url = os.getenv("BASE_URL")
#     username = os.getenv("API_USERNAME")
#     password = os.getenv("PASSWORD")
#
#     url = f"{base_url}/post"
#     payload = {"username": username, "password": password}
#     resp = requests.post(url, json=payload)
#     assert resp.status_code == 200
#     token = resp.json()["json"]["username"] + "_token"
#     return token
#
#
# @pytest.fixture(scope="session")
# def auth_token():
#     print("\n>>> 登录一次，获取 token（整个会话只执行一次）")
#     token = login()
#     return token
#
#
# def test_api_1(auth_token):
#     print(f"\n测试1 使用的 token: {auth_token}")
#     assert True
#
#
# def test_api_2(auth_token):
#     print(f"\n测试2 使用的 token: {auth_token}")
#     assert True


# import os
# import requests
# import pytest
# from dotenv import load_dotenv
#
#
# # 加载 .env 文件中的环境变量（默认读取 .env 文件）
# load_dotenv()
#
# # 从环境变量读取配置
# BASE_URL = os.getenv("BASE_URL")
# USERNAME = os.getenv("API_USERNAME")   # 避免与 Windows 系统变量冲突
# PASSWORD = os.getenv("PASSWORD")
#
# def login():
#     """模拟登录：发送 POST 请求，从响应中提取用户名，拼接 token"""
#     url = f"{BASE_URL}/post"
#     payload = {"username": USERNAME, "password": PASSWORD}
#     resp = requests.post(url, json=payload)
#     # 先断言状态码成功
#     assert resp.status_code == 200, f"登录失败，状态码：{resp.status_code}"
#     # 解析 JSON
#     data = resp.json()
#     # 从响应的 json 字段中取回 username（httpbin 会原样返回）
#     returned_username = data["json"]["username"]
#     # 模拟服务端生成的 token（真实项目通常从响应中直接取 token 字段）
#     token = returned_username + "_token"
#     return token
#
# @pytest.fixture(scope="session")
# def auth_token():
#     """整个测试会话只登录一次，返回 token"""
#     print("\n>>> 执行登录，获取 token（整个会话只一次）")
#     token = login()
#     return token
#
# def test_bearer_check(auth_token):
#     """测试1：使用 token 访问 /bearer 端点"""
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     url = f"{BASE_URL}/bearer"
#     resp = requests.get(url, headers=headers)
#     assert resp.status_code == 200
#     data = resp.json()
#     # /bearer 会返回 token 字段，值应该和我们发送的一样
#     assert data["token"] == auth_token
#     print(f"\n测试1 通过，token 验证成功: {auth_token}")
#
# def test_anything_check(auth_token):
#     """测试2：使用 token 访问 /anything 端点，验证请求头中的 Authorization"""
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     url = f"{BASE_URL}/anything"
#     resp = requests.get(url, headers=headers)
#     assert resp.status_code == 200
#     data = resp.json()
#     # 检查响应中 headers 下的 Authorization 字段
#     # httpbin 返回的 headers 中键名为 "Authorization"（首字母大写）
#     assert data["headers"].get("Authorization") == f"Bearer {auth_token}"
#     print(f"\n测试2 通过，请求头中的 Authorization 正确: Bearer {auth_token}")
#
# if __name__ == "__main__":
#     # 方便直接运行此文件（非 pytest 方式），但推荐用 pytest 命令
#     pytest.main([__file__, "-v", "--html=report.html", "--self-contained-html"])


import os
import requests
import pytest
from dotenv import load_dotenv
import logging

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

# 加载 .env 文件中的环境变量（默认读取 .env 文件）
load_dotenv()

# 从环境变量读取配置
BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("API_USERNAME")   # 避免与 Windows 系统变量冲突
PASSWORD = os.getenv("PASSWORD")

def login():
    """模拟登录：发送 POST 请求，从响应中提取用户名，拼接 token"""
    url = f"{BASE_URL}/post"
    payload = {"username": USERNAME, "password": PASSWORD}
    resp = requests.post(url, json=payload)
    # 先断言状态码成功
    assert resp.status_code == 200, f"登录失败，状态码：{resp.status_code}"
    # 解析 JSON
    data = resp.json()
    # 从响应的 json 字段中取回 username（httpbin 会原样返回）
    returned_username = data["json"]["username"]
    # 模拟服务端生成的 token（真实项目通常从响应中直接取 token 字段）
    token = returned_username + "_token"
    return token

@pytest.fixture(scope="session")
def auth_token():
    """整个测试会话只登录一次，返回 token"""
    logging.info("执行登录，获取 token（整个会话只一次）")
    token = login()
    return token

def test_bearer_check(auth_token):
    """测试1：使用 token 访问 /bearer 端点"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    url = f"{BASE_URL}/bearer"
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    # /bearer 会返回 token 字段，值应该和我们发送的一样
    assert data["token"] == auth_token
    logging.info(f"测试1 通过，token 验证成功: {auth_token}")

def test_anything_check(auth_token):
    """测试2：使用 token 访问 /anything 端点，验证请求头中的 Authorization"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    url = f"{BASE_URL}/anything"
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    # 检查响应中 headers 下的 Authorization 字段
    # httpbin 返回的 headers 中键名为 "Authorization"（首字母大写）
    assert data["headers"].get("Authorization") == f"Bearer {auth_token}"
    logging.info(f"测试2 通过，请求头中的 Authorization 正确: Bearer {auth_token}")

if __name__ == "__main__":
    # 方便直接运行此文件（非 pytest 方式），但推荐用 pytest 命令
    pytest.main([__file__, "-v", "--html=report.html", "--self-contained-html"])