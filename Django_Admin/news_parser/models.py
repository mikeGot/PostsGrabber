import uuid
from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    tag = models.CharField("tag", max_length=128)
    date = models.DateTimeField("datetime")
    message = models.TextField("message")

    class Meta:
        db_table = "posts"
        verbose_name = "Post"

    def __repr__(self):
        return f"{self.tag} : {self.message[:10] if self.message else []}"


class Urls(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    url = models.URLField("url")

    class Meta:
        db_table = "urls"
        verbose_name = "Url"

    def __repr__(self):
        return self.url


class Polls(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    question = models.TextField("Question", max_length=256, blank=True)

    class Meta:
        db_table = "polls"
        verbose_name = "Poll"

    def __repr__(self):
        return self.question
