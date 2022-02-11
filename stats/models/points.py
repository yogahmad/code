from django.db import models

from commons.models import BaseModel


class PointManager(models.Manager):
    pass


class Point(BaseModel):
    class PointType:
        MINUTES = "minutes"
        GOALS_SCORED = "goals_scored"
        ASSISTS = "assists"
        CLEAN_SHEETS = "clean_sheets"
        GOALS_CONCEDED = "goals_conceded"
        OWN_GOALS = "own_goals"
        PENALTIES_SAVED = "penalties_saved"
        PENALTIES_MISSED = "penalties_missed"
        YELLOW_CARDS = "yellow_cards"
        RED_CARDS = "red_cards"
        SAVES = "saves"
        BONUS = "bonus"

    POINT_TYPE_CHOICES = {
        PointType.MINUTES: "Minutes",
        PointType.GOALS_SCORED: "Goals scored",
        PointType.ASSISTS: "Assists",
        PointType.CLEAN_SHEETS: "Clean sheets",
        PointType.GOALS_CONCEDED: "Goals conceded",
        PointType.OWN_GOALS: "Own goals",
        PointType.PENALTIES_SAVED: "Penalties saved",
        PointType.PENALTIES_MISSED: "Penalties missed",
        PointType.YELLOW_CARDS: "Yellow cards",
        PointType.RED_CARDS: "Red cards",
        PointType.SAVES: "Saves",
        PointType.BONUS: "Bonus",
    }

    identifier = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        choices=POINT_TYPE_CHOICES.items(),
    )
    player = models.ForeignKey(
        "players.Player",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="points",
    )
    match = models.ForeignKey(
        "matches.Match",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="points",
    )
    number = models.IntegerField(blank=False, null=False, default=0)

    objects = PointManager()

    class Meta:
        unique_together = (
            "identifier",
            "player",
            "match",
        )
