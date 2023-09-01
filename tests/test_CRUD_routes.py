from app import app, test_client


def test_simple():
    mylist = [1, 2, 3, 4]

    assert 3 in mylist


def test_get_route():
    res = test_client.get('/tutorial')
    assert res.status_code == 200
    assert len(res.get_json()) == 2


def test_post_route():
    data = {
        'id': 3,
        'name': 'Unit tests',
        'description': 'Testing routes with pytest'
    }
    res = test_client.post('/tutorial', json=data)
    assert res.status_code == 200
    assert len(res.get_json()) == 3
    assert res.get_json()[-1]['name'] == 'Unit tests'


