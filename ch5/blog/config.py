# -*- coding: utf-8 -*-
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = '.env'
