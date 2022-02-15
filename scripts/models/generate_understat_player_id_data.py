from django.core.exceptions import ValidationError
from django.db import models

from commons.models import BaseModel


class GenerateUnderstatPlayerIdData(BaseModel):
    understat_team_id = models.CharField(max_length=32)
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Generate understat player id data"
