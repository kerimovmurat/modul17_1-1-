from fastapi import FastAPI
from app.routers import category

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My shop"}

app.include_router(category.router)