import csv
import pytest
import requests

def load_users():
    """从 CSV 文件读取数据，返回列表，每个元素是 (user_id, expected_name)"""
    users = []
    with open('users.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # 自动把第一行当作列名
        for row in reader:
            user_id = int(row['user_id'])
            expected_name = row['expected_name']
            users.append((user_id, expected_name))
    return users

@pytest.mark.parametrize("user_id, expected_name", load_users())


def test_user_from_csv(user_id, expected_name):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    resp = requests.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == expected_name