from pydantic import BaseModel, UUID4, Extra

class MenuIn(BaseModel):
    title: str
    description: str

class MenuOut(MenuIn):
    id: UUID4
    submenus_count: int
    dishes_count: int

    class Config:
        orm_mode = True


class SubmenuIn(BaseModel):
    title: str
    description: str


class SubmenuOut(SubmenuIn):
    id: UUID4
    dishes_count: int

    class Config:
        orm_mode = True


class DishIn(BaseModel):
    title: str
    description: str
    price: str


class DishOut(DishIn):
    id: UUID4

    class Config:
        orm_mode = True

