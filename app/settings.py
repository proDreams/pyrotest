from typing import Union

from pydantic import SecretStr, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings
from pyrogram import Client
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.utils.redis_storage import RedisStorage


class Secrets(BaseSettings):
    api_id: Union[SecretStr.get_secret_value, int]
    api_hash: SecretStr
    admin_id: Union[SecretStr.get_secret_value, int]
    db_url: PostgresDsn
    redis: RedisDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


secrets = Secrets()

engine = create_async_engine(url=secrets.db_url.unicode_string())
sessionmaker = async_sessionmaker(engine, expire_on_commit=False, autocommit=False)

redis_storage = RedisStorage(Redis(host="127.0.0.1", decode_responses=True))

client = Client(
    name="myapp",
    api_id=secrets.api_id,
    api_hash=secrets.api_hash.get_secret_value(),
)
