from sqlalchemy.orm import Session
from app.sql import models, schemas
from app.repository import bll
import json


# region User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# endregion User

# region Triplet
def get_triplets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Triplet).offset(skip).limit(limit).all()


def create_triplets(db: Session):
    x = 0
    triplet_data = bll.create_all_triplets()
    triplets = json.loads(triplet_data)
    for (k, v) in triplets:
        db.execute(f"INSERT INTO triplets (pattern) VALUES ('{triplets[x][v]}')")
        x = x + 1
    db.commit()


# endregion


# region Cuarta
def get_cuartas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cuarta).offset(skip).limit(limit).all()


def create_cuartas(db: Session):
    x = 0
    cuarta_data = bll.create_all_cuartas()
    cuartas = json.loads(cuarta_data)
    for (k, v) in cuartas:
        db.execute(f"INSERT INTO cuartas (pattern) VALUES ('{cuartas[x][v]}')")
        x = x + 1
    db.commit()
# endregion
