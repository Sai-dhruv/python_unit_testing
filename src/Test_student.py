from StudentDB import *
import pytest


@pytest.mark.parametrize('arg1, result',
                         [
                             ('id', 1),
                             ('name', 'Scott'),
                             ('result', 'Pass')

                         ])
def test_using_parametrize(arg1, result):
    db = StudentDB()
    db.connect('student.json')
    scott_data = db.get_data('Scott')
    assert scott_data[arg1] == result


def test_scot_data():
    db = StudentDB()
    db.connect('student.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'Pass'


def test_mark_data():
    db = StudentDB()
    db.connect('student.json')
    scott_data = db.get_data('mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'mark'
    assert scott_data['result'] == 'fail'
