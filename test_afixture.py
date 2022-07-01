from StudentDB import StudentDB
import pytest

# @pytest.fixture(scope='module')
# def db():
#     print('---setup_module---')
#     db = StudentDB()
#     db.connect('data.json')
#     yield db
#     print('---tearDown_module---')
#     db.close()

def test_hung_data():
    db = StudentDB()
    db.connect('data.json')
    hung_data = db.get_data('Hung')
    assert hung_data['id'] == 1
    assert hung_data['name'] == 'Hung'
    assert hung_data['result'] == 'pass'

def test_hai_data():
    db = StudentDB()
    db.connect('data.json')
    hai_data = db.get_data('Hai')
    assert hai_data['id'] == 2
    assert hai_data['name'] == 'Hai'
    assert hai_data['result'] == 'pass'