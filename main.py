import uvicorn
from fastapi.routing import APIRouter

from fastapi import Depends, FastAPI

from app.routes.dish_router import dish_router
from app.routes.menu_router import menu_router
from app.routes.submenu_router import submenu_router
from app.services.dish_services import DishService
from app.services.submenu_services import SubmenuService
from app.services.menu_services import MenuService

from app.core.database import Base, SessionLocal, engine, get_db


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(menu_router, prefix='/api/v1/menus', tags=['menu'])
app.include_router(submenu_router, prefix='/api/v1/menus/{menu_id}/submenus', tags=['submenu'])
app.include_router(dish_router,
                               prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes',
                               tags=['dish'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)