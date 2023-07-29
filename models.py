import uuid

from sqlalchemy import Column, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Menu(Base):
    __tablename__ = "menus"

    id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), index=True)
    description = Column(String(125))

    submenus = relationship("Submenu", back_populates='menu', cascade='all, delete-orphan')


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), index=True)
    description = Column(String(125))
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id"))

    dishes = relationship("Dish", back_populates="submenu", cascade='all, delete-orphan')
    menu = relationship("Menu", back_populates="submenus")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), index=True)
    description = Column(String(125))
    price = Column(Numeric(precision=10, scale=2))
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("submenus.id"))

    submenu = relationship("Submenu", back_populates="dishes")
