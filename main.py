from typing import List, Dict
import uvicorn

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas import DishIn, DishOut, SubmenuIn, SubmenuOut, MenuIn, MenuOut
from models import Dish, Menu, Submenu, Base
from database import SessionLocal, engine
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##################
# Endpoint of Dish
##################

@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishOut)
def read_dish(dish_id: str, db: Session = Depends(get_db)):
    db_dish = crud.get_dish(db, dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish


@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', response_model=List[DishOut])
def read_list_dishes(db: Session = Depends(get_db)):
    db_list_dishes = crud.get_dishes(db)
    return db_list_dishes


@app.post('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', response_model=DishOut, status_code=201)
def create_dish(dish: DishIn, submenu_id: str, db: Session = Depends(get_db)):
    db_dish = crud.create_dish(db, dish, submenu_id)
    return db_dish


@app.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishOut)
def update_dish(dish_id: str, dish: DishIn, db: Session = Depends(get_db)):
    db_dish = crud.update_dish(db, dish, dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish

@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def delete_dish(dish_id: str, db: Session = Depends(get_db)) -> Dict[str, str | bool]:
    db_dish = crud.delete_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish

#####################
# Endpoint of Submenu
#####################

@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}', response_model=SubmenuOut)
def read_submenu(submenu_id: str, db: Session = Depends(get_db)):
    db_submenu = crud.get_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@app.get('/api/v1/menus/{menu_id}/submenus', response_model=List[SubmenuOut])
def read_list_submenus(db: Session = Depends(get_db)):
    return crud.get_submenus(db)


@app.post('/api/v1/menus/{menu_id}/submenus', response_model=SubmenuOut, status_code=201)
def create_submenu(submenu: SubmenuIn, menu_id: str,
                   db: Session = Depends(get_db)):
    db_submenu = crud.create_submenu(db, submenu, menu_id)
    db_submenu.dishes_count = 0
    return db_submenu


@app.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}',
           response_model=SubmenuOut)
def update_submenu(submenu_id: str, submenu: SubmenuIn,
                   db: Session = Depends(get_db)):
    db_submenu = crud.update_submenu(db, submenu, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def delete_submenu(submenu_id: str, db: Session = Depends(get_db)) -> Dict[str, str | bool]:
    db_submenu = crud.delete_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu

##################
# Endpoint of Menu
##################

@app.get('/api/v1/menus/{menu_id}',
         response_model=MenuOut)
def read_menu(menu_id: str, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu
#
#
@app.get('/api/v1/menus',
         response_model=List[MenuOut])
def read_list_menus(db: Session = Depends(get_db)):
    return crud.get_menus(db)



@app.post('/api/v1/menus',
          response_model=MenuOut, status_code=201)
def create_menu(menu: MenuIn, db: Session = Depends(get_db)):
    db_menu = crud.create_menu(db, menu)
    db_menu.submenus_count = 0
    db_menu.dishes_count = 0
    return db_menu


@app.patch('/api/v1/menus/{menu_id}',
           response_model=MenuOut)
def update_menu(menu_id: str, menu: MenuIn, db: Session = Depends(get_db)):
    db_menu = crud.update_menu(db, menu, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.delete('/api/v1/menus/{menu_id}')
def delete_menu(menu_id: str, db: Session = Depends(get_db)) -> Dict[str, str | bool]:
    db_menu = crud.delete_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu
