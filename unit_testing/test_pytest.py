# PyTest
from unit_testing.simplecalc import SimpleCalc
import pytest


@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_addition(calc):
    # calc = SimpleCalc()
    assert calc.add(6, 2) == 8


def test_calc_subtraction(calc):
    # calc = SimpleCalc()
    assert calc.sub(6, 2) == 4


def test_calc_multiplication(calc):
    # calc = SimpleCalc()
    assert pytest.approx(calc.multi(0.4, -80.9)) == -32.36


def test_calc_division(calc):
    # calc = SimpleCalc()
    assert calc.divide(6, 2) == 3


def test_calc_divide_by_zero_raises_error(calc):
    # calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
