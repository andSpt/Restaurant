from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from app.core.models import Dish
from app.core.schemas import DishIn
from app.core.database import get_db


class DishRepository:

    def __init__(self, session: Session = Depends(get_db)):
        self.session: Session = session
        self.model = Dish

    def get_all(self) -> list[Dish]:
        return self.session.query(self.model).all()

    def get(self, dish_id: str) -> Dish:
        item = self.session.query(self.model).filter(self.model.id == dish_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="dish not found")
        return item

    def create(self, item_data: DishIn, submenu_id: str) -> Dish:
        item = self.model(title=item_data.title, description=item_data.description,
                          price=item_data.price, submenu_id=submenu_id)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def update(self, item_data: DishIn, dish_id: str) -> Dish:
        item = self.get(dish_id)
        if not item:
            raise HTTPException(status_code=404, detail="dish not found")
        item.title = item_data.title
        item.description = item_data.description
        item.price = item_data.price
        self.session.commit()
        self.session.refresh(item)
        return item


    def delete(self, dish_id: str) -> dict[str, str | bool]:
        item = self.get(dish_id)
        if not item:
            raise HTTPException(status_code=404, detail="dish not found")
        self.session.delete(item)
        self.session.commit()
        return {"status": True,
                "message": "The dish has been deleted"}
