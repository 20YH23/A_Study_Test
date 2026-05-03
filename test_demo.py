import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 4),
    (4, 5, 9),
    (0, 0, 0),
])


def test_add(a, b, expected):
    assert a + b == expected