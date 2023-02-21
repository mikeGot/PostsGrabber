import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import db_models
from core.configuration import settings
from models import Post

engine = create_engine(settings.sqlite_dsn, echo=True, future=True)


def insert_to_db(tag: str, data: list[Post]):
    with Session(engine) as session:
        add_posts: list[db_models.Post] = []
        add_urls: list[db_models.Urls] = []
        add_polls: list[db_models.Polls] = []

        for post in data:
            post_id = str(uuid.uuid4())

            add_posts.append(
                db_models.Post(
                    id=post_id, tag=tag, date=post.date, message=post.message
                )
            )

            if post.media and post.media.poll:
                add_polls.append(
                    db_models.Polls(
                        post_id_id=post_id, question=post.media.poll.question
                    )
                )

            for entity in post.entities:
                if entity.url:
                    add_urls.append(
                        db_models.Urls(
                            id=str(uuid.uuid4()), post_id_id=post_id, url=entity.url
                        )
                    )

        session.add_all(add_posts)
        session.add_all(add_polls)
        session.add_all(add_urls)
        session.commit()
