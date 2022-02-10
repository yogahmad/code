from django.db import models

from commons.models import BaseModel


class PreviousSeasonTotalPointManager(models.Manager):
    pass


class PreviousSeasonTotalPoint(BaseModel):
    class PreviousSeasonTotalPointPointType:
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
        PreviousSeasonTotalPointPointType.MINUTES: "minutes",
        PreviousSeasonTotalPointPointType.GOALS_SCORED: "goals_scored",
        PreviousSeasonTotalPointPointType.ASSISTS: "assists",
        PreviousSeasonTotalPointPointType.CLEAN_SHEETS: "clean_sheets",
        PreviousSeasonTotalPointPointType.GOALS_CONCEDED: "goals_conceded",
        PreviousSeasonTotalPointPointType.OWN_GOALS: "own_goals",
        PreviousSeasonTotalPointPointType.PENALTIES_SAVED: "penalties_saved",
        PreviousSeasonTotalPointPointType.PENALTIES_MISSED: "penalties_missed",
        PreviousSeasonTotalPointPointType.YELLOW_CARDS: "yellow_cards",
        PreviousSeasonTotalPointPointType.RED_CARDS: "red_cards",
        PreviousSeasonTotalPointPointType.SAVES: "saves",
        PreviousSeasonTotalPointPointType.BONUS: "bonus",
    }

    season = models.CharField(max_length=32, blank=False, null=False)
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
        related_name="previous_season_points",
    )
    match = models.ForeignKey(
        "matches.Match",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="previous_season_points",
    )
    number = models.IntegerField(blank=False, null=False, default=0)

    objects = PreviousSeasonTotalPointManager()
