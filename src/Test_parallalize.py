import Math_function as mf
import pytest


@pytest.mark.parametrize('num1,num2,result',
                         [
                             (2, 3, 5),
                             (2.0, 3.0, 5.0),
                             ('sai', 'krishna', 'saikrishna')

                         ])
def test_def_add(num1, num2, result):
    assert mf.add(num1, num2) == result

