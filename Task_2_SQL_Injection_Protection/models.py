from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100)
    )

    email = Column(
        String(100),
        unique=True
    )

    encrypted_password = Column(
        String(500)
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )