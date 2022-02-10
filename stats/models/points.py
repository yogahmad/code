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
        PointType.MINUTES: "minutes",
        PointType.GOALS_SCORED: "goals_scored",
        PointType.ASSISTS: "assists",
        PointType.CLEAN_SHEETS: "clean_sheets",
        PointType.GOALS_CONCEDED: "goals_conceded",
        PointType.OWN_GOALS: "own_goals",
        PointType.PENALTIES_SAVED: "penalties_saved",
        PointType.PENALTIES_MISSED: "penalties_missed",
        PointType.YELLOW_CARDS: "yellow_cards",
        PointType.RED_CARDS: "red_cards",
        PointType.SAVES: "saves",
        PointType.BONUS: "bonus",
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
