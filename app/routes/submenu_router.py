from typing import List, Dict
from fastapi import APIRouter

from fastapi import Depends, HTTPException

from app.core.schemas import SubmenuIn, SubmenuOut
from app.services.submenu_services import SubmenuService
from app.core.database import get_db


submenu_router = APIRouter()


@submenu_router.get('/{submenu_id}', response_model=SubmenuOut)
def get_submenu(submenu_id: str, submenu: SubmenuService = Depends()):
    '''Возвращает подменю с количеством всех блюд'''
    return submenu.get(submenu_id)


@submenu_router.get('/', response_model=List[SubmenuOut])
def get_submenus(submenu: SubmenuService = Depends()):
    '''Возвращает список подменю с количеством всех блюд'''
    return submenu.get_all()


@submenu_router.post('/', response_model=SubmenuOut, status_code=201)
def create_submenu(item_data: SubmenuIn, menu_id: str, submenu: SubmenuService = Depends()):
    '''Создает подменю c количеством блюд равным 0'''
    return submenu.create(item_data, menu_id)


@submenu_router.patch('/{submenu_id}', response_model=SubmenuOut)
def update_submenu(item_data: SubmenuIn, submenu_id: str, submenu: SubmenuService = Depends()):
    '''Обновляет подменю'''
    return submenu.update(item_data, submenu_id)


@submenu_router.delete('/{submenu_id}')
def delete_submenu(submenu_id: str, submenu: SubmenuService = Depends()) -> Dict[str, str | bool]:
    '''Удаляет подменю'''
    return submenu.delete(submenu_id)
