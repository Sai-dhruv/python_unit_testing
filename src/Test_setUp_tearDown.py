from StudentDB import *
import pytest

db = None


def setup_module(module):
    print("From Set up")
    global db
    db = StudentDB()
    db.connect('student.json')


def teardown_module(module):
    print("Tear Down")
    db.close()


def test_scot_data():
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'Pass'


def test_mark_data():
    scott_data = db.get_data('mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'mark'
    assert scott_data['result'] == 'fail'
