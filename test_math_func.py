import math_func
import pytest
import sys

# @pytest.mark.skip(reason='do not run number add test')
def test_add():
    assert math_func.add(3, 4) == 7
    assert math_func.add(3, -4) == -1   

# @pytest.mark.skipif(sys.version_info < (3, 6), reason='requires python3.6 or higher')
def test_product():
    assert math_func.product(3, 4) == 12
    assert math_func.product(3, -4) == -12

#@pytest.mark.strings
def test_add_strings():
    assert math_func.add('3', '4') == '34'
    assert math_func.add('3', '-4') == '3-4'
#@pytest.mark.strings
def test_product_strings():
    assert math_func.product('3', '4') == '12'
    assert math_func.product('3', '-4') == '-12'

# def test_add_float():
#     assert math_func.add(3.0, 4.0) == 7.0
#     assert math_func.add(3.0, -4.0) == -1.0

