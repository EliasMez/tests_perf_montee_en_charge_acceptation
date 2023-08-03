from calculatrice import additionner, soustraire, factorial_recursive
import pytest

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0
    assert additionner([1, 2, 3], 4) == 10

def test_soustraire():
    assert soustraire(5, 3) == 2

@pytest.mark.parametrize("n, expected_result", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial_recursive(n, expected_result):
    assert factorial_recursive(n) == expected_result

def test_factorial_recursive_performance(benchmark):
    n = 20
    benchmark(factorial_recursive, n)