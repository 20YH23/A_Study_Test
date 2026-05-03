import pytest
import requests

@pytest.mark.parametrize("title, body, userId", [
    ("foo", "bar", 1),
    ("hello", "world", 2),
    ("pytest", "参数化测试", 3),
])


def test_create_posts(title, body, userId):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": userId
    }
    resp = requests.post(url, json=payload)
    assert resp.status_code == 201   # 创建成功返回201
    data = resp.json()
    # 断言返回的数据与发送的数据一致（服务器会回显这些字段）
    assert data["title"] == title
    assert data["body"] == body
    assert data["userId"] == userId
    # 此外还会返回一个自动生成的 id
    assert "id" in data