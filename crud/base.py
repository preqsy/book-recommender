from typing import Generic
from typing import Type, TypeVar

from bson import ObjectId
from pydantic import BaseModel
from pymongo.database import Database
from pymongo.collection import Collection

from models.base import BaseBaseModel

ModelType = TypeVar("ModelType", bound=BaseBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):

    def __init__(self, db: Database, model: Type[ModelType]):
        self.db = db
        self.model = model
        self.collection_name = self.model.__collection_name__
        self._db: Collection = self.db[self.collection_name]

    def get_single_item(self, id: ObjectId) -> dict:
        query = self._db.find_one({"_id": ObjectId(id)})
        return query if query else None

    def create(self, data_dict: dict):
        new_item_id = self._db.insert_one(data_dict).inserted_id
        return self.model(**data_dict)
