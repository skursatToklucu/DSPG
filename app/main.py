from typing import Optional
from fastapi import FastAPI
from app.schemas.user import User
import json

app = FastAPI()


# uvicorn app.main:app

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def read_users():
    users = User.query.all()
    return await json.dumps(users)


@app.post("/new-user")
async def get_body(user: User):
    return await user.json()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
