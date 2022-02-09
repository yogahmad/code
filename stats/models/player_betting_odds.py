from django.db import models

from commons.models import BaseModel


class PlayerBettingOddManager(models.Manager):
    pass


class PlayerBettingOdd(BaseModel):
    class OddType:
        GOALS_SCORED = "goals_scored"
        ASSISTS = "assists"

    ODD_TYPE_CHOICES = {
        OddType.GOALS_SCORED: "goals_scored",
        OddType.ASSISTS: "assists",
    }

    identifier = models.CharField(
        max_length=32, blank=False, null=False, choices=ODD_TYPE_CHOICES.items()
    )
    player = models.ForeignKey(
        "players.Player",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="player_betting_odds",
    )
    match = models.ForeignKey(
        "matches.Match",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="player_betting_odds",
    )
    odd = models.FloatField(blank=False, null=False, default=0.0)

    objects = PlayerBettingOddManager()
