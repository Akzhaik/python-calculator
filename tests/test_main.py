from src.main import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15


def test_divide():
    assert divide(10, 2) == 5

from src.main import square_root


def test_square_root():
    assert square_root(25) == 5


def test_square_root_zero():
    assert square_root(0) == 0