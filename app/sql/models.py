from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.sql.database import Base, engine
from alembic import op
from app.repository import bll
from sqlalchemy.sql import table, column


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # items = relationship("Item", back_populates="owner")


class Triplet(Base):
    __tablename__ = "triplets"
    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String)


class Cuarta(Base):
    __tablename__ = "cuartas"
    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String)


class Quintuplet(Base):
    __tablename__ = "quintuplets"
    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String)


class Sextuplet(Base):
    __tablename__ = "sextuplets"
    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String)


class Septuplet(Base):
    __tablename__ = "septuplets"
    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String)


Base.metadata.create_all(bind=engine)
