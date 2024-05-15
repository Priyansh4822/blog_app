from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schema import Blog, BlogCreate
from src.database import SessionLocal
from src.serializers.blog_serializer import get_blog, get_blogs, create_blog, update_blog, delete_blog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/blogs/", response_model=Blog)
def create_new_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db=db, blog=blog)

@router.get("/blogs/", response_model=List[Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_blogs(db=db, skip=skip, limit=limit)

@router.get("/blogs/{blog_id}", response_model=Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = get_blog(db=db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.put("/blogs/{blog_id}", response_model=Blog)
def update_existing_blog(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = update_blog(db=db, blog_id=blog_id, blog=blog)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.delete("/blogs/{blog_id}")
def delete_existing_blog(blog_id: int, db: Session = Depends(get_db)):
    success = delete_blog(db=db, blog_id=blog_id)
    if not success:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}
