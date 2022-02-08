import sqlalchemy.sql
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


def filter_cuartas(db: Session, skip: int = 0, limit: int = 10, search_filter: str = ' '):
    return db.query(models.Cuarta).filter_by(pattern=search_filter).first()


# endregion

# region Quintuplet
def get_quintuplets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quintuplet).offset(skip).limit(limit).all()


def create_quintuplets(db: Session):
    x = 0
    quin_data = bll.create_all_quintuplets()
    quintets = json.loads(quin_data)
    for (k, v) in quintets:
        db.execute(f"INSERT INTO quintuplets (pattern) VALUES('{quintets[x][v]}')")
        x = x + 1
    db.commit()


# endregion


# region Sextuplet
def get_sextuplets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sextuplet).offset(skip).limit(limit).all()


def create_sextuplets(db: Session):
    x = 0
    sextup_data = bll.create_all_sextuplet()
    sextuplets = json.loads(sextup_data)
    for (k, v) in sextuplets:
        db.execute(f"INSERT INTO sextuplets (pattern) VALUES('{sextuplets[x][v]}')")
        x = x + 1
    db.commit()


# endregion

# region Septuplet
def get_septuplets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Septuplet).offset(skip).limit(limit).all()


def create_septuplets(db: Session):
    x = 0
    septup_data = bll.create_all_septuplet()
    septuplets = json.loads(septup_data)
    for (k, v) in septuplets:
        db.execute(f"INSERT INTO septuplets (pattern) VALUES('{septuplets[x][v]}')")
        x = x + 1
    db.commit()
# endregion
