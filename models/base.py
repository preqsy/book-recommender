from datetime import datetime
from typing import Any, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field, GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic_core import CoreSchema, core_schema


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None, config=None):
        if not ObjectId.is_valid(v):
            raise ValueError(f"{v} is not a valid ObjectId")

        return str(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema, core_schema: GetCoreSchemaHandler
    ) -> CoreSchema:
        # TODO: Fix this so response models/OpenAI docs will work
        # print(f"Core {core_schema}")
        # print(f"Core Schema Type{type(core_schema)}")
        # core_schema.update(type="string")
        schema.update(type="string")

        return schema

    # @classmethod
    # def __get_pydantic_json_schema__(
    #     cls, schema: CoreSchema, handler: GetJsonSchemaHandler
    # ) -> dict[str, Any]:
    #     """This hooks into the low-level schema generation system to customize the enum JSON schema"""
    #     json_schema = handler(schema)
    #     json_schema = handler.resolve_ref_schema(json_schema)
    #     json_schema.update(
    #         {
    #             "enum": [x.name for x in cls],
    #             "type": "string",
    #         }
    #     )
    #     return json_schema


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
