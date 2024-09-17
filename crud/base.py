from typing import Generic
from typing import Type, TypeVar

from bson import ObjectId
from pydantic import BaseModel
from pymongo.database import Database
from pymongo.collection import Collection

ModelType = TypeVar("ModelType", bound=BaseModel)


class CRUDBase:
    def __init__(self, db: Database, collection_name):
        self.db = db
        self.collection_name = collection_name
        self._db: Collection = self.db[self.collection_name]

    def get_single_item(self, id: ObjectId) -> dict:
        query = self._db.find_one({"_id": ObjectId(id)})
        return query if query else None

    def create(self, data_dict: dict):
        new_item_id = self._db.insert_one(data_dict)
        print(new_item_id)
        return new_item_id
