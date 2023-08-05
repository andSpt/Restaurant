from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from app.core.models import Menu
from app.core.schemas import MenuIn, MenuOut
from app.core.database import get_db, SessionLocal


class MenuRepository:

    def __init__(self, session: Session = Depends(get_db)):
        self.session: Session = session
        self.model = Menu

    def get_all(self) -> list[Menu]:
        items = self.session.query(self.model).all()
        list_items = []
        if items == []:
            return items
        for item in items:
            item.submenus_count = str(len(item.submenus))
            item.dishes_count = str(sum(len(submenu.dishes) for submenu in item.submenus))
            list_items.append(item)
        return list_items

    def get(self, menu_id: str) -> Menu:
        item = self.session.query(self.model).filter(self.model.id == menu_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="menu not found")
        item.submenus_count = (len(item.submenus))
        item.dishes_count = sum(len(submenu.dishes) for submenu in item.submenus)
        return item

    def create(self, item_data: MenuIn) -> Menu:
        item = self.model(title=item_data.title, description=item_data.description)
        item.submenus_count = 0
        item.dishes_count = 0
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def update(self, item_data: MenuIn, menu_id: str) -> Menu:
        item = self.get(menu_id)
        if not item:
            raise HTTPException(status_code=404, detail="menu not found")
        item.title = item_data.title
        item.description = item_data.description
        self.session.commit()
        self.session.refresh(item)
        return item

    def delete(self, menu_id: str) -> dict[str, str | bool]:
        item = self.get(menu_id)
        if not item:
            raise HTTPException(status_code=404, detail="menu not found")
        self.session.delete(item)
        self.session.commit()
        return {"status": True,
                "message": "The menu has been deleted"}
