from StudentDB import *
import pytest


@pytest.fixture(scope='module')
def db():
    print("----------------Set up-------------------")
    db = StudentDB()
    db.connect('student.json')
    # return db
    yield db
    print("Tear Down -------------")
    db.close()


def test_scot_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'Pass'


def test_mark_data(db):
    scott_data = db.get_data('mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'mark'
    assert scott_data['result'] == 'fail'
