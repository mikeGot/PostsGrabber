import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Text, DateTime
from sqlalchemy import (ARRAY, Column)

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"
    id: str = Column(primary_key=True)
    tag: str = Column()
    date: datetime = Column(DateTime)
    message: str = Column()


class Urls(Base):
    __tablename__ = "urls"
    id: str = Column(primary_key=True, default=str(uuid.uuid4()))
    post_id_id: str = Column()
    url: str = Column(String)


class Polls(Base):
    __tablename__ = "polls"
    id: str = Column(primary_key=True, default=str(uuid.uuid4()))
    post_id_id: str = Column()
    question: str = Column()
