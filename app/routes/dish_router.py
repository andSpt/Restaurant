from typing import List, Dict
from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.schemas import DishIn, DishOut
from app.core.database import get_db
from app.services.dish_services import DishService


dish_router = APIRouter()


@dish_router.get('/{dish_id}', response_model=DishOut)
def get_dish(dish_id: str, dish: DishService = Depends()):
    '''Возвращает блюдо'''
    return dish.get(dish_id)


@dish_router.get('/', response_model=List[DishOut])
def get_dishes(dish: DishService = Depends()):
    '''Возвращает список всех блюд'''
    return dish.get_all()


@dish_router.post('/', response_model=DishOut, status_code=201)
def create_dish(item_data: DishIn, submenu_id: str, dish: DishService = Depends()):
    '''Создает новое блюдо'''
    return dish.create(item_data, submenu_id)


@dish_router.patch('/{dish_id}', response_model=DishOut)
def update_dish(dish_id: str, item_data: DishIn, dish: DishService = Depends()):
    '''Обновляет блюдо'''
    return dish.update(item_data, dish_id)


@dish_router.delete('/{dish_id}')
def delete_dish(dish_id: str, dish: DishService = Depends()) -> Dict[str, str | bool]:
    '''Удаляет блюдо'''
    return dish.delete(dish_id)