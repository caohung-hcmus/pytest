from logging import warning
import pytest
from yaml import warnings

def test_passing():
    assert(1, 2, 3) == (1, 2, 3)
def test_failing():
    assert(1, 2, 3) == (3, 2, 1)

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0

# def test_warning():
#     with pytest.warns(UserWarning):
#         warnings.warns("This is a warning", UserWarning)