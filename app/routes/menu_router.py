from typing import List, Dict
import uvicorn
from fastapi import APIRouter

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.schemas import MenuIn, MenuOut
from app.core.database import get_db
from app.services.menu_services import MenuService


menu_router = APIRouter()


@menu_router.get('/{menu_id}', response_model=MenuOut)
def get_menu(menu_id: str, menu: MenuService = Depends()):
    '''Возвращает меню с количеством всех подменю и блюд'''
    return menu.get(menu_id)


@menu_router.get('/', response_model=List[MenuOut])
def get_menus(menu: MenuService = Depends()):
    '''Возвращает список меню с количеством всех подменю и блюд'''
    return menu.get_all()


@menu_router.post('/', response_model=MenuOut, status_code=201)
def create_menu(item_data: MenuIn, menu: MenuService = Depends()):
    '''Создает меню с количеством подменю и блюд равным нулю'''
    return menu.create(item_data)


@menu_router.patch('/{menu_id}', response_model=MenuOut)
def update_menu(menu_id: str, item_data: MenuIn, menu: MenuService = Depends()):
    '''Обновляет меню'''
    return menu.update(item_data, menu_id)


@menu_router.delete('/{menu_id}')
def delete_menu(menu_id: str, menu: MenuService = Depends()) -> Dict[str, str | bool]:
    '''Удаляет меню'''
    return menu.delete(menu_id)