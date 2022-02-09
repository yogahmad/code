from django.db import models

from commons.models import BaseModel


class TeamBettingOddManager(models.Manager):
    pass


class TeamBettingOdd(BaseModel):
    class OddType:
        CLEAN_SHEETS = "clean_sheets"

    ODD_TYPE_CHOICES = {
        OddType.CLEAN_SHEETS: "clean_sheets",
    }

    identifier = models.CharField(
        max_length=32, blank=False, null=False, choices=ODD_TYPE_CHOICES.items()
    )
    team = models.ForeignKey(
        "teams.Team",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="team_betting_odds",
    )
    match = models.ForeignKey(
        "matches.Match",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="team_betting_odds",
    )
    odd = models.FloatField(blank=False, null=False, default=0.0)

    objects = TeamBettingOddManager()
