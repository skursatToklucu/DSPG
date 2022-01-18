from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from app.sql import crud, models, schemas
from app.sql.database import SessionLocal, engine
from app.repository import bll

# uvicorn app.main:app
app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# region User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Böyle bir email zaten kayıtlı!")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Böyle bir kullanıcı bulunmamaktadır!")
    return db_user


# endregion

@app.post("/triplets/", response_model=schemas.Triplet)
def create_triplets(db: Session = Depends(get_db)):
    return crud.create_triplets(db)


@app.get("/triplets/", response_model=list[schemas.Triplet])
def read_triplets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    triplets = crud.get_triplets(db, skip=skip, limit=limit)
    return triplets


@app.post("/cuartas/", response_model=schemas.Triplet)
def create_cuartas(db: Session = Depends(get_db)):
    return crud.create_cuartas(db)


@app.get("/cuartas/", response_model=list[schemas.Triplet])
def read_cuartas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cuartas = crud.get_cuartas(db, skip=skip, limit=limit)
    return cuartas
