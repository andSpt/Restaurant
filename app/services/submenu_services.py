from fastapi import Depends, HTTPException

from app.core.models import Submenu
from app.core.schemas import SubmenuIn, SubmenuOut
from app.core.repositories.submenu_repository import SubmenuRepository


# class CacheRepository:
#
#     def __init__(self):
#         self.redis =


class SubmenuService:

    def __init__(self, database_repository: SubmenuRepository = Depends()):
        self.database_repository = database_repository

    def get_all(self) -> list[Submenu]:
        return self.database_repository.get_all()

    def get(self, submenu_id) -> Submenu:
        return self.database_repository.get(submenu_id)

    def create(self, item_data: SubmenuIn, menu_id: str) -> Submenu:
        return self.database_repository.create(item_data, menu_id)

    def update(self, item_data: SubmenuIn, submenu_id) -> Submenu:
        return self.database_repository.update(item_data, submenu_id)

    def delete(self, submenu_id) -> dict[str, str | bool]:
        return self.database_repository.delete(submenu_id)
