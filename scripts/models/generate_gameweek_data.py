from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from commons.models import BaseModel
from scripts.constants import \
    START_GAMEWEEK_MUST_BE_LESS_THAN_OR_EQUAL_TO_END_GAMEWEEK


class GenerateGameweekData(BaseModel):
    start_gameweek = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(38),
        ],
    )
    end_gameweek = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(38)],
    )

    def clean(self) -> None:
        if self.start_gameweek > self.end_gameweek:
            raise ValidationError(
                START_GAMEWEEK_MUST_BE_LESS_THAN_OR_EQUAL_TO_END_GAMEWEEK
            )
        return super().clean()
