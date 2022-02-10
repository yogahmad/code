from django.db import models

from commons.models import BaseModel


class TeamManager(models.Manager):
    pass


class Team(BaseModel):
    fpl_id = models.IntegerField(blank=False, null=False, unique=True)
    name = models.CharField(blank=False, null=False, unique=True, max_length=128)
    short_name = models.CharField(blank=False, null=False, unique=True, max_length=10)
    strength_attack_home = models.IntegerField(blank=False, null=False, default=0)
    strength_attack_away = models.IntegerField(blank=False, null=False, default=0)
    strength_defence_home = models.IntegerField(blank=False, null=False, default=0)
    strength_defence_away = models.IntegerField(blank=False, null=False, default=0)
    kit = models.ForeignKey(
        "kits.Kit",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="teams",
    )

    objects = TeamManager()