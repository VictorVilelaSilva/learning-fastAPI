from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}

    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, ALGORITHM)

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1',
        headers={'Authorization': 'Bearer token-invalido'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_without_token_subject(client):
    token = create_access_token(data={})
    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_with_non_existent_user(client):
    token = create_access_token(data={'sub': 'non_existent_user@example.com'})
    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
