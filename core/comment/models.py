from django.db import models
from core.abstract.models import AbstractManager,AbstractModel

# Create your models here.

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    post = models.ForeignKey("core_post.Post",on_delete=models.PROTECT)
    author = models.ForeignKey("core_user.User",on_delete=models.PROTECT)

    body = models.CharField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name