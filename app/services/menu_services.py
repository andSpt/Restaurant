from fastapi import Depends, HTTPException

from app.core.models import Menu
from app.core.schemas import MenuIn, MenuOut
from app.core.repositories.menu_repository import MenuRepository
from app.core.database import get_db


# class CacheRepository:
#
#     def __init__(self):
#         self.redis =


class MenuService:

    def __init__(self, database_repository: MenuRepository = Depends()):
        self.database_repository = database_repository

    def get_all(self) -> list[Menu]:
        return self.database_repository.get_all()

    def get(self, menu_id) -> Menu:
        return self.database_repository.get(menu_id)

    def create(self, item_data: MenuIn) -> Menu:
        return self.database_repository.create(item_data)

    def update(self, item_data: MenuIn, menu_id) -> Menu:
        return self.database_repository.update(item_data, menu_id)

    def delete(self, menu_id) -> dict[str, str | bool]:
        return self.database_repository.delete(menu_id)

