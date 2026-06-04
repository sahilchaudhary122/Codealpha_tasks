from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class Customer(Base):
    __tablename__ = "customers"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    name = Column(
        String(100)
    )
    email = Column(
        String(100) ,
        unique=True
    )
    phone = Column(
        String(20),
        unique=True
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )