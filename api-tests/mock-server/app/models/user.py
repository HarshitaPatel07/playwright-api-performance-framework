from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    
    name = Column(String, nullable=False)

    email = Column(String, nullable=False, unique=True)

    gender = Column(String, nullable=False)

    age = Column(Integer, nullable=False)
