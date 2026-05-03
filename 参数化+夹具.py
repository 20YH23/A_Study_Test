import pytest
import requests

# 夹具：提供 token（模拟登录）
@pytest.fixture(scope="session")
def auth_token():
    print("\n>>> 执行登录，获取 token（整个会话只一次）")
    resp = requests.post("https://httpbin.org/post", json={"user": "tester"})
    assert resp.status_code == 200
    token = resp.json()["json"]["user"] + "_token"
    return token

# 参数化：四个参数
@pytest.mark.parametrize("product_id, quantity, payment_method, expected_status", [
    (101, 1, "credit_card", 201),
    (102, 2, "paypal", 201),
    (103, 0, "credit_card", 400),   # 数量为0，预期失败
    (104, 1, "invalid", 422),        # 无效支付方式
])

def test_create_order(auth_token, product_id, quantity, payment_method, expected_status):
    headers = {"Authorization": f"Bearer {auth_token}"}
    url = "https://api.example.com/orders"  # 这里是假地址，实际需替换
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "payment_method": payment_method
    }
    # 实际项目中要替换成真实接口
    resp = requests.post(url, json=payload, headers=headers)
    assert resp.status_code == expected_status