import Math_function as mf
import pytest


@pytest.mark.number
def test_add():
    assert mf.add(10, 12) == 22
    assert mf.add(10) == 12


@pytest.mark.number
def test_mul():
    assert mf.mul(10, 5) == 50
    assert mf.mul(10) == 20


@pytest.mark.string
def test_add_string():
    result = mf.add('sai', 'krishna')
    assert result == 'saikrishna'
    assert type(result) == str
    assert 'abc' not in result

@pytest.mark.string
def test_mul_string():
    result = mf.mul('sai',3)
    print(result)
    assert result == 'saisaisai'
