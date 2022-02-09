from django.db import models

from commons.models import BaseModel


class BonusPointSystemManager(models.Manager):
    pass


class BonusPointSystem(BaseModel):
    point = models.IntegerField(blank=False, null=False, default=0)
    player = models.ForeignKey(
        "players.Player",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="bpses",
    )
    match = models.ForeignKey(
        "matches.Match",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="bpses",
    )

    objects = BonusPointSystemManager()
