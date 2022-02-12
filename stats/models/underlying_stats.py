from django.db import models

from commons.models import BaseModel


class UnderlyingStatManager(models.Manager):
    pass


class UnderlyingStat(BaseModel):
    npxG = models.FloatField(blank=False, null=False)
    xA = models.FloatField(blank=False, null=False)
    shots = models.IntegerField(blank=False, null=False)
    key_passes = models.IntegerField(blank=False, null=False)
    match = models.ForeignKey(
        "matches.Match", blank=False, null=False, on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural = "Underlying stat"
