from django.db import models

from commons.models import BaseModel


class GameweekManager(models.Manager):
    pass


class Gameweek(BaseModel):
    number = models.IntegerField(blank=False, null=False, unique=True)

    objects = GameweekManager()

    def __str__(self):
        return "Gameweek {}".format(self.number)
