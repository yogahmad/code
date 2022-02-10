from django.db import models

from commons.models import BaseModel


class ShotsDataManager(models.Manager):
    pass


class ShotsData(BaseModel):
    class ShotResultType:
        GOAL = "Goal"
        SAVED = "SavedShot"
        BLOCKED = "BlockedShot"
        MISSED = "MissedShots"

    SHOT_RESULT_TYPE_CHOICES = {
        ShotResultType.GOAL: "Goal",
        ShotResultType.SAVED: "Saved",
        ShotResultType.BLOCKED: "Blocked",
        ShotResultType.MISSED: "Missed",
    }

    player = models.ForeignKey(
        "players.Player",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="shots_data",
    )
    player_assisted = models.ForeignKey(
        "players.Player",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="assist_shots_data",
    )
    expected_goal = models.FloatField(blank=False, null=False)
    match = models.ForeignKey(
        "matches.Match",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="shots_data",
    )
    result = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        choices=SHOT_RESULT_TYPE_CHOICES.items(),
    )
    minute = models.CharField(max_length=32, null=False, blank=False)
