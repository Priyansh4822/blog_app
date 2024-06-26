from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author = Column(String)
    published = Column(Boolean, default=False)
