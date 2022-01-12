from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1956Colaiuta.@localhost/DspaceDB"
SQLALCHEMY_DATABASE_URI = "sqlite:///./dspace.db"

# connect_args sadece sql_lite kullanma ihtimaline karşı yazdım diğer databaseler için gerek yok

# POSTGRE SQL için Engine
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URI
# )

# SQL Lite için
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
