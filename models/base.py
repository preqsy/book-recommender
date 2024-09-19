from datetime import datetime
from typing import Any, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"{v} is not a valid ObjectId")

        return str(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, core_schema):
        print(f"Schema {schema}")
        print(f"Schema Type{type(schema)}")
        print(f"Core {core_schema}")
        print(f"Core Schema Type{type(core_schema)}")
        schema.update(type="string")
        return schema


class WBase(BaseModel):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        _id = data.get("_id")
        if _id:
            self.id = PyObjectId.validate(_id)


class BaseBaseModel(WBase):
    __collection_name__ = ""
    id: Optional[PyObjectId] = None
    created_timestamp: datetime = Field(default=datetime.utcnow())
    updated_timestamp: Optional[datetime] = None
