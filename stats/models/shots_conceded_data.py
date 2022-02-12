from django.db import models

from commons.models import BaseModel


class ShotsConcededDataManager(models.Manager):
    pass


class ShotsConcededData(BaseModel):
    class ShotResultType:
        GOAL = "Goal"
        SAVED = "SavedShot"
        BLOCKED = "BlockedShot"
        MISSED = "MissedShots"
        SHOT_ON_POST = "ShotOnPost"

    SHOT_RESULT_TYPE_CHOICES = {
        ShotResultType.GOAL: "Goal",
        ShotResultType.SAVED: "Saved",
        ShotResultType.BLOCKED: "Blocked",
        ShotResultType.MISSED: "Missed",
        ShotResultType.SHOT_ON_POST: "Shot On Post",
    }

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
    team = models.ForeignKey(
        "teams.Team",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Shots conceded data"
