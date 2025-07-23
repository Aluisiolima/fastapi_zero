from pydantic import BaseModel


class SchemaBase(BaseModel):
    class Config:
        extra = 'ignore'
        from_attributes = True
