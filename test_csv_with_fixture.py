import csv
import pytest
import requests

# ---------- 夹具：获取 token（整个 session 一次） ----------
@pytest.fixture(scope="session")
def auth_token():
    print("\n>>> 执行登录（整个会话一次），获取 token")
    # 使用 httpbin 的 /post 模拟登录，实际项目换成真实接口
    url = "https://httpbin.org/post"
    payload = {"username": "testuser", "password": "123456"}
    resp = requests.post(url, json=payload)
    assert resp.status_code == 200
    data = resp.json()
    # 模拟 token（真实项目从 data["token"] 取）
    token = data["json"]["username"] + "_token"
    return token

# ---------- 从 CSV 读取数据（返回元组列表） ----------
def load_users_from_csv():
    data = []
    with open("users.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)   # 第一行作为列名
        for row in reader:
            uid = int(row["user_id"])
            name = row["expected_name"]
            data.append((uid, name))
    return data

# ---------- 测试函数：同时使用夹具和 CSV 参数化 ----------
@pytest.mark.parametrize("uid, expected_name", load_users_from_csv())


def test_user_info(auth_token, uid, expected_name):
    headers = {"Authorization": f"Bearer {auth_token}"}
    # 这里用 jsonplaceholder 的公开接口演示（实际不需要 token，仅示范）
    url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    resp = requests.get(url, headers=headers)   # headers 虽然对 jsonplaceholder 无用，但展示用法
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == expected_name
    print(f"\n用户 {uid} 断言通过，name = {expected_name}")