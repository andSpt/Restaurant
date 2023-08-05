from fastapi import Depends, HTTPException

from app.core.models import Dish
from app.core.schemas import DishIn, DishOut
from app.core.repositories.dish_repository import DishRepository


# class CacheRepository:
#
#     def __init__(self):
#         self.redis =


class DishService:

    def __init__(self, database_repository: DishRepository = Depends()):
        self.database_repository = database_repository

    def get_all(self) -> list[Dish]:
        return self.database_repository.get_all()

    def get(self, dish_id) -> Dish:
        return self.database_repository.get(dish_id)

    def create(self, item_data: DishIn, submenu_id: str) -> Dish:
        return self.database_repository.create(item_data, submenu_id)

    def update(self, item_data: DishIn, dish_id) -> Dish:
        return self.database_repository.update(item_data, dish_id)

    def delete(self, dish_id) -> dict[str, str | bool]:
        return self.database_repository.delete(dish_id)
