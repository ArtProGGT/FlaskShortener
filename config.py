from os import getenv


class Config:
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
