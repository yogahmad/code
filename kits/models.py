from django.db import models

from commons.models import BaseModel


class KitManager(models.Manager):
    pass


class Kit(BaseModel):
    url = models.URLField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=32)
    objects = KitManager()
