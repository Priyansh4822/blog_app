from sqlalchemy.orm import Session
from src.models import Blog
from src.schema import BlogCreate

def get_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Blog).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: BlogCreate):
    db_blog = Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if db_blog is None:
        return None
    for key, value in blog.dict().items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return True
    return False
