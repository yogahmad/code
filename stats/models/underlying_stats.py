from django.db import models

from commons.models import BaseModel


class UnderlyingStatManager(models.Manager):
    pass


class UnderlyingStat(BaseModel):
    xG = models.FloatField(blank=False, null=False)
    xA = models.FloatField(blank=False, null=False)
    shots = models.IntegerField(blank=False, null=False)
    key_passes = models.IntegerField(blank=False, null=False)
    match = models.ForeignKey(
        "matches.Match", blank=False, null=False, on_delete=models.CASCADE,)
    player = models.ForeignKey(
        "players.Player", blank=False, null=False, on_delete=models.CASCADE,)
    minutes = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        unique_together = (
            "match",
            "player",
        )
        verbose_name_plural = "Underlying stat"
