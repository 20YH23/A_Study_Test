import requests


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    resp = requests.post(url, json=payload)

    assert resp.status_code == 201  # 201 表示创建成功
    data = resp.json()
    assert data["title"] == "foo"
    assert data["userId"] == 1
    # 服务器会返回一个自动生成的 id，断言它存在即可
    assert "id" in data