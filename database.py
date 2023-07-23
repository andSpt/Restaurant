from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import load_config


config = load_config('.env')

SQLALCHEMY_DATABASE_URL = f"postgresql://{config.db.db_user}:" \
                          f"{config.db.db_password}@" \
                          f"{config.db.db_host}:" \
                          f"{config.db.db_port}/" \
                          f"{config.db.database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
