from sum_two import sum_two


def test_sum_positive():
    assert sum_two(1, 2) == 3


def test_sum_negative():
    assert sum_two(-1, -2) == -3


def test_sum_mix():
    assert sum_two(2.5, 1.5) == 4.0
