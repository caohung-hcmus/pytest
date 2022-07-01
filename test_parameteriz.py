import pytest
import math_func

def test_Add():
    assert math_func.add(3, 4) == 7
    expected = math_func.add('hello', 'world')
    assert expected == 'helloworld'
    expected = math_func.add(3.0, 4.0)
    assert expected == 7.0


@pytest.mark.parametrize('x, y, expected', [ (7,3,10), ('Hello', 'World', 'HelloWorld'), (3.0, 4.0, 7.0)])
def test_add_with_parameters(x, y, expected):
    assert math_func.add(x, y) == expected