from django.db import models
import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AbstractManager(models.Manager):
    def get_object_by_id(self,id):
        try:
            instance = self.get(public_id=id)
            return instance
        except (ObjectDoesNotExist,ValueError,TypeError):
            return Http404

class AbstractModel(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,db_index=True,unique=True,editable=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = AbstractManager()

    class Meta:
        abstract=True