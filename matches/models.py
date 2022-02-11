from django.db import models

from commons.models import BaseModel


class MatchManager(models.Manager):
    pass


class Match(BaseModel):
    fpl_id = models.IntegerField(blank=False, null=False, unique=True)
    home_team = models.ForeignKey(
        "teams.Team",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="home_matches",
    )
    away_team = models.ForeignKey(
        "teams.Team",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="away_matches",
    )
    gameweek = models.ForeignKey(
        "gameweeks.Gameweek",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="matches",
    )

    objects = MatchManager()

    class Meta:
        unique_together = (
            "home_team",
            "away_team",
        )
        verbose_name_plural = "Matches"

    def __str__(self):
        return "{} vs {}".format(self.home_team.name, self.away_team.name)
