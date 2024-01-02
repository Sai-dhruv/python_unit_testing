from python_unit_testing.src import Math_function as mf


def test_add():
    assert mf.add(10, 12) == 22
    assert mf.add(2) == 4
