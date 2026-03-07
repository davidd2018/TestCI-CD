from sum import sum

def test_sum_basic():
    assert sum(5, 3) == 8
    assert sum(0, 0) == 0
    assert sum(-1, 1) == 0
