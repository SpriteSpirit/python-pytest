from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2], -1, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5, 6], 23, "test") == "test"


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2], -1, 2) == [2]
    assert arrs.my_slice([1, 2], None, 2) == [1, 2]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([1, 3, 5], None, None) == [1, 3, 5]
