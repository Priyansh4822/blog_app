from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str
    author: str
    published: Optional[bool] = False

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True
