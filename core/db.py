from pymongo import MongoClient
from core import settings


def get_db():
    client = MongoClient(settings.DATABASE_URL)
    database = client[settings.DB_NAME]

    yield database
