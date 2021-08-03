from pydantic import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str
