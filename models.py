from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Poll(BaseModel):
    id: str | None
    question: str
    answers: list[dict] | None


class Photo(BaseModel):
    id: str | None
    file_reference: bytes | None
    date: datetime | None


class Entity(BaseModel):
    url: str | None


class Media(BaseModel):
    poll: Poll | None
    results: dict | None
    photo: Photo | None


class Post(BaseModel):
    date: datetime
    message: str | None
    media: Media | None
    entities: list[Entity] | None
