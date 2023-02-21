import datetime

from Django_Admin.news_parser.models import Post
from uuid import uuid4

post = Post(id=uuid4(), tag='yandex', date=datetime.datetime.now(), message="hello").save()

