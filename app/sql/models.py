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


# triplet_data = bll.create_all_triplets()
# print(triplet_data)
# triplet_table = table('triplets', column('id', Integer), column('pattern', String))
#
# op.bulk_insert(triplet_table, triplet_data)
Base.metadata.create_all(bind=engine)

# İlişki Örneği için
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")
