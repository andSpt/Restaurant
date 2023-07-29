from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# from config import load_config


# config = load_config()

DATABASE_URL = 'postgresql://postgres:root@postgres_ylab:5432/ylab'
# DATABASE_URL = f"postgresql://{config.db.postgres_user}:" \
#                f"{config.db.postgres_password}@postgres_ylab:5432/{config.db.postgres_db}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
