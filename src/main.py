from fastapi import FastAPI
from src.database import engine, Base
from src.controllers import blog_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog_controller.router, prefix="/api")
