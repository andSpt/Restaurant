from fastapi.testclient import TestClient
from main import app
import crud

import pytest

client = TestClient(app)

BASE_URL = "http://0.0.0.0:8000/api/v1/menus"

menu_data = {
    'title': 'My menu 1',
    'description': 'My menu description 1'
}

submenu_data = {
    'title': 'My submenu 1',
    'description': 'My submenu description 1'
}

dish_data = {
    'title': 'My dish 1',
    'description': 'My dish description 1',
    'price': '12.50'
}


def test_get_empty_list_menus():
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


def test_get_empty_list_submenus():
    response = client.get(f"{BASE_URL}/{menu_data.get('id')}/submenus")
    assert response.status_code == 200
    assert response.json() == []


def test_create_submenu():
    response = client.post(f"{BASE_URL}/{menu_data.get('id')}/submenus", json=submenu_data)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert submenu_data['title'] == response.json().get('title')
    assert submenu_data['description'] == response.json().get('description')

    submenu_data['id'] = response.json().get('id')


def test_get_list_submenus():
    response = client.get(f"{BASE_URL}/{menu_data.get('id')}/submenus")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_submenu():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}")
    assert response.status_code == 200
    assert response.json().get('id') == submenu_data.get('id')


def test_get_empty_list_dishes():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/dishes")
    assert response.status_code == 200
    assert response.json() == []


def test_create_dish():
    response = client.post(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/dishes",
        json=dish_data)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert dish_data['title'] == response.json().get('title')
    assert dish_data['description'] == response.json().get('description')
    assert dish_data['price'] == response.json().get('price')

    dish_data['id'] = response.json().get('id')


def test_get_list_dishes():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/dishes")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_dish():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/dishes/{dish_data.get('id')}")
    assert response.status_code == 200
    assert response.json().get('id') == dish_data.get('id')


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


def test_update_submenu():
    update_data = {
        'title': 'My updated submenu 1',
        'description': 'My updated submenu description 1',
    }
    response = client.patch(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}",
        json=update_data)
    assert response.status_code == 200

    submenu_data['title'] = update_data['title']
    submenu_data['description'] = update_data['description']

    update_response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}")
    assert update_response.status_code == 200
    assert update_response.json().get('id') == submenu_data.get('id')
    assert update_response.json().get('title') == submenu_data.get('title')
    assert update_response.json().get('description') == submenu_data.get('description')


def test_update_dish():
    update_data = {
        'title': 'My updated dish 1',
        'description': 'My updated dish description 1',
        'price': '14.50'
    }
    response = client.patch(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/"
        f"dishes/{dish_data.get('id')}",
        json=update_data)
    assert response.status_code == 200

    dish_data['title'] = update_data['title']
    dish_data['description'] = update_data['description']
    dish_data['price'] = update_data['price']

    update_response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/"
        f"dishes/{dish_data.get('id')}")
    assert update_response.status_code == 200
    assert update_response.json().get('id') == dish_data.get('id')
    assert update_response.json().get('title') == dish_data.get('title')
    assert update_response.json().get('description') == dish_data.get('description')
    assert update_response.json().get('price') == dish_data.get('price')


def test_delete_dish():
    response = client.delete(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/"
        f"dishes/{dish_data.get('id')}")
    assert response.status_code == 200


def test_get_empty_list_dishes_after_delete():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/dishes")
    assert response.status_code == 200
    assert response.json() == []


def test_get_dish_after_delete():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}/"
        f"dishes/{dish_data.get('id')}")
    assert response.status_code == 404
    assert response.json().get('detail') == 'dish not found'


def test_delete_submenu():
    response = client.delete(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}")
    assert response.status_code == 200


def test_get_empty_list_submenus_after_delete():
    response = client.get(f"{BASE_URL}/{menu_data.get('id')}/submenus")
    assert response.status_code == 200
    assert response.json() == []


def test_get_submenu_after_delete():
    response = client.get(
        f"{BASE_URL}/{menu_data.get('id')}/submenus/{submenu_data.get('id')}")
    assert response.status_code == 404
    assert response.json().get('detail') == 'submenu not found'


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


def test_get_empty_list_menu():
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == []
