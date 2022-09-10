from test_reqres_api.conftest import *


def test_register():
    response = api().post('register', json={
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    })

    assert response.status_code == 200
    assert S(register) == response.json()
    assert int(response.json()['id']) == 4


def test_login():
    response = api().post(
        'login', json={
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'
        })

    assert response.status_code == 200
    assert S(login) == response.json()
    assert str(response.json()['token']) == 'QpwL5tke4Pnpja7X4'


def test_create():
    response = api().post(
        'users', json={
            'name': 'Anna',
            'job': 'QA'
        })
    assert response.status_code == 201
    assert S(create) == response.json()
    assert str(response.json()['name']) == 'Anna'
    assert str(response.json()['job']) == 'QA'


def test_update():
    response = api().put('users/345', json={
        'name': 'Nina',
        'job': 'QA Auto'
    })

    assert response.status_code == 200
    assert S(update) == response.json()
    assert str(response.json()['name']) == 'Nina'
    assert str(response.json()['job']) == 'QA Auto'


def test_delete():
    response = api().delete(
        'users/345')

    assert response.status_code == 204
