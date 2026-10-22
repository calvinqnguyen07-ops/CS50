import pytest

from mathtools import factorial, fibonacci, is_prime


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (2, True),
    (9, False),
    (97, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-3)
