from pymongo import MongoClient
from pymongo.errors import AutoReconnect
from core.config import settings
import logging

print(settings.DATABASE_URL)
print(settings.DB_NAME)
print(settings.COLLECTION_NAME)


def get_db():
    client = MongoClient(settings.DATABASE_URL)
    database = client[settings.DB_NAME]

    yield database
