from fastapi_zero.core import SchemaBase


class CategoryCreated(SchemaBase):
    pass


class CategoryUpdated(SchemaBase):
    pass


class CategoryResponse(SchemaBase):
    id: int
    name: int
