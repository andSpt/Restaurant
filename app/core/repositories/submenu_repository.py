from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from app.core.models import Submenu
from app.core.schemas import SubmenuIn, SubmenuOut
from app.core.database import get_db


class SubmenuRepository:

    def __init__(self, session: Session = Depends(get_db)):
        self.session: Session = session
        self.model = Submenu

    def get_all(self) -> list[Submenu]:
        items = self.session.query(self.model).all()
        list_items = []
        if items:
            for item in items:
                item.dishes_count = len(item.dishes)
                list_items.append(item)
            return list_items
        return []

    def get(self, submenu_id: str) -> Submenu:
        item = self.session.query(self.model).filter(self.model.id == submenu_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="submenu not found")
        item.dishes_count = len(item.dishes)
        return item

    def create(self, item_data: SubmenuIn, menu_id: str) -> Submenu:
        item = self.model(title=item_data.title, description=item_data.description,
                          menu_id=menu_id)
        item.dishes_count = 0
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def update(self, item_data: SubmenuIn, submenu_id: str) -> Submenu:
        item = self.get(submenu_id)
        if not item:
            raise HTTPException(status_code=404, detail="submenu not found")
        item.title = item_data.title
        item.description = item_data.description
        self.session.commit()
        self.session.refresh(item)
        return item

    def delete(self, submenu_id: str) -> dict[str, str | bool]:
        item = self.get(submenu_id)
        if not item:
            raise HTTPException(status_code=404, detail="submenu not found")
        self.session.delete(item)
        self.session.commit()
        return {"status": True,
                "message": "The submenu has been deleted"}
