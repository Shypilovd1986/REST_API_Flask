from app import test_client
from app.models.models import Student


def test_simple():
    mylist = [1, 2, 3, 4]

    assert 3 in mylist


def test_get_route():
    res = test_client.get('/list_of_students')
    assert res.status_code == 200
    # assert len(res.get_json()) == 2


def test_post_route():
    data = {
        'user_name': 'Sam',
        'user_surname': 'Boby',
        'email': 'sam@mail.com',
        'password': '123n13'
    }
    res = test_client.post('/registration', json=data)
    assert res.status_code == 200
    # assert len(res.get_json()) == 3
    # assert res.get_json()[-1]['name'] == 'Unit tests'


def test_put_route():
    res = test_client.put('/personal_information/3', json={'email': 'value_error@mail.ru'})
    assert res.status_code == 200
    assert Student.query.get(3).email == 'value_error@mail.ru'


def test_delete_route():
    res = test_client.delete('/personal_information/7')
    assert res.status_code == 204
    assert Student.query.get(6) is None
