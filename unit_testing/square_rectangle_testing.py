from unit_testing.squares_rectangles import rectangle
from unit_testing.squares_rectangles import square
import pytest


@pytest.fixture
def test_area_rec():
    assert rectangle(4, 5).area_calc() == 20


def test_area_sqr():
    assert square(4).area_calc() == 16


def test_perm_rec():
    assert rectangle(4, 5).perimeter_calc() == 18


def test_perm_sqr():
    assert square(4).perimeter_calc() == 16


def test_number():
    assert square(4).number_surrounding(square(1)) == 16
