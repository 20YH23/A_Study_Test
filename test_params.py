import requests


def test_get_with_params():
    url = "https://jsonplaceholder.typicode.com/posts"
    # 模拟分页和筛选参数
    params = {
        "userId": 1,
        "_limit": 2  # 限制返回条数（该 API 支持）
    }
    resp = requests.get(url, params=params)

    assert resp.status_code == 200
    data = resp.json()
    # 断言返回的是列表，且长度不超过 2
    assert isinstance(data, list)
    assert len(data) <= 2
    # 断言每条数据的 userId 都是 1
    for post in data:
        assert post["userId"] == 1
    print("实际请求的 URL:", resp.url)  # 你会看到 ?userId=1&_limit=2