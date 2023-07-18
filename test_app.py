from app import add_nums


def test_add_nums():
    a, b = 2, 3
    assert add_nums(a, b) == 5
