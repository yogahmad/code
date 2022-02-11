from django.db import models

from commons.models import BaseModel


class GeneratePlayersPointData(BaseModel):
    team = models.ForeignKey(
        "teams.Team",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="generate_players_point_data",
    )
    gameweek = models.ForeignKey(
        "gameweeks.Gameweek",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="generate_players_point_data",
    )

    class Meta:
        verbose_name_plural = "Generate players point data"
