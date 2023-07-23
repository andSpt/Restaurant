from sqlalchemy.orm import Session

from models import Dish, Menu, Submenu
from schemas import DishIn, DishOut, SubmenuIn, SubmenuOut, MenuIn, MenuOut


##############
# CRUD of Dish
##############

def get_dish(db: Session, dish_id: str):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def get_dishes(db: Session) -> list:
    db_dishes = db.query(Dish).all()
    return db_dishes


def create_dish(db: Session, dish: DishIn, submenu_id: str):
    db_dish = Dish(title=dish.title, description=dish.description, price=dish.price,
                   submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def update_dish(db: Session, dish: DishIn, dish_id: str):
    db_dish = get_dish(db, dish_id)
    if db_dish:
        db_dish.title = dish.title
        db_dish.description = dish.description
        db_dish.price = dish.price
        db.commit()
        db.refresh(db_dish)
        return db_dish


def delete_dish(db: Session, dish_id: str):
    db_dish = get_dish(db, dish_id)
    if db_dish:
        db.delete(db_dish)
        db.commit()
        return {"status": True,
                "message": "The dish has been deleted"}


#################
# CRUD of Submenu
#################

def get_submenu(db: Session, submenu_id: str):
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    if db_submenu:
        db_submenu.dishes_count = len(db_submenu.dishes)
        return db_submenu


def get_submenus(db: Session):
    db_submenus = db.query(Submenu).all()
    list_db_submenus = []
    if db_submenus:
        for db_submenu in db_submenus:
            db_submenu.dishes_count = len(db_submenu.dishes)
            list_db_submenus.append(db_submenu)
        return list_db_submenus
    return []


def create_submenu(db: Session, submenu: SubmenuIn, menu_id: str):
    db_submenu = Submenu(title=submenu.title, description=submenu.description, menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def update_submenu(db: Session, submenu: SubmenuIn, submenu_id: str):
    db_submenu = get_submenu(db, submenu_id)
    if db_submenu:
        db_submenu.title = submenu.title
        db_submenu.description = submenu.description
        db.commit()
        db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, submenu_id: str):
    db_submenu = get_submenu(db, submenu_id)
    if db_submenu:
        db.delete(db_submenu)
        db.commit()
        return {"status": True,
                "message": "The submenu has been deleted"}


##############
# CRUD of Menu
##############


def get_menus(db: Session):
    db_menus = db.query(Menu).all()
    list_db_menus = []
    if db_menus:
        for db_menu in db_menus:
            db_menu.submenus_count = str(len(db_menu.submenus))
            db_menu.dishes_count = str(
                sum(len(submenu.dishes) for submenu in db_menu.submenus))
            list_db_menus.append(db_menu)
        return list_db_menus
    return []


def get_menu(db: Session, menu_id: str):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if db_menu:
        db_menu.submenus_count = (len(db_menu.submenus))
        db_menu.dishes_count = sum(len(submenu.dishes) for submenu in db_menu.submenus)
        return db_menu


def create_menu(db: Session, menu: MenuIn):
    db_menu = Menu(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def update_menu(db: Session, menu: MenuIn, menu_id):
    db_menu = get_menu(db, menu_id)
    if db_menu:
        db_menu.title = menu.title
        db_menu.description = menu.description
        db.commit()
        db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: str):
    db_menu = get_menu(db, menu_id)
    if db_menu:
        db.delete(db_menu)
        db.commit()
        return {"status": True,
                "message": "The menu has been deleted"}
