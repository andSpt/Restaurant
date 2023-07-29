from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    postgres_user: str
    postgres_password: str
    postgres_db: str
    pguser: str


@dataclass
class Config:
    db: DatabaseConfig


def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(db=DatabaseConfig(postgres_user=env('POSTGRES_USER'),
                                    postgres_password=env('POSTGRES_PASSWORD'),
                                    postgres_db=env('POSTGRES_DB'),
                                    pguser=env('PGUSER'))
                  )
