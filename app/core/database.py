import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import load_config


conf = load_config('.env')

DATABASE_URL = f"postgresql://{conf.db.postgres_user}:" \
               f"{conf.db.postgres_password}@postgres_ylab:5432/{conf.db.postgres_db}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()