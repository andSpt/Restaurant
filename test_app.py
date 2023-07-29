from fastapi.testclient import TestClient
from main import app
import crud

import pytest

client = TestClient(app)

BASE_URL = "http://0.0.0.0:8000/api/v1/menus"

menu_data = {'title': 'My menu 1', 'description': 'My menu description 1'}


@pytest.fixture()
def submenu_data():
    return {
        'title': 'My submenu 1',
        'description': 'My submenu description 1'
    }


def test_get_empty_list_menu():
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == []


def test_create_menu():
    response = client.post(BASE_URL, json=menu_data)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert menu_data['title'] == response.json().get('title')
    assert menu_data['description'] == response.json().get('description')

    menu_data['id'] = response.json().get('id')


def test_get_list_menus():
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_menu():
    response = client.get(f"{BASE_URL}/{menu_data.get('id')}")
    assert response.status_code == 200
    assert response.json().get('id') == menu_data.get('id')


def test_update_menu():
    update_data = {
        'title': 'My updated menu 1',
        'description': 'My updated menu description 1'
    }
    response = client.patch(f"{BASE_URL}/{menu_data.get('id')}", json=update_data)
    assert response.status_code == 200

    menu_data['title'] = update_data['title']
    menu_data['description'] = update_data['description']

    update_response = client.get(f"{BASE_URL}/{menu_data.get('id')}")
    assert update_response.status_code == 200
    assert update_response.json().get('id') == menu_data.get('id')
    assert update_response.json().get('title') == menu_data.get('title')
    assert update_response.json().get('description') == menu_data.get('description')


def test_delete_menu():
    response = client.delete(f"{BASE_URL}/{menu_data.get('id')}")
    assert response.status_code == 200


def test_get_empty_list_menus_after_delete():
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == []


def test_get_menu_after_delete():
    response = client.get(f"{BASE_URL}/{menu_data.get('id')}")
    assert response.status_code == 404
    assert response.json().get('detail') == 'menu not found'
