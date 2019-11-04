from smbla import add


def test_test():
    assert add(2, 2) == 4
    assert add(1, 2) == 3
    assert add(4, 2) == 6
    assert add(0, 0) == 0
