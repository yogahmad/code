from django.db import models
from django.db.models import Q, Sum

from commons.models import BaseModel
from gameweeks.models import Gameweek
from stats.models.underlying_stats import UnderlyingStat


class TeamManager(models.Manager):
    pass


class Team(BaseModel):
    fpl_id = models.IntegerField(blank=False, null=False, unique=True)
    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=128,
    )
    short_name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=10,
    )
    strength_attack_home = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    strength_attack_away = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    strength_defence_home = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    strength_defence_away = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    kit = models.ForeignKey(
        "kits.Kit",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="teams",
    )
    understat_id = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
    )

    @property
    def xg_form(self):
        form = 0.0
        percentage = 0
        for gameweek_number in range(1, 28):
            gameweek = Gameweek.objects.get(number=gameweek_number)
            matches = gameweek.matches.filter(
                Q(away_team=self) | Q(home_team=self)
            )
            for match in matches:
                base_qs = UnderlyingStat.objects.filter(
                    match=match, player__team=self)

                if not base_qs.exists():
                    continue

                form *= 15 / 17
                percentage *= 15 / 17

                xG = base_qs.aggregate(Sum("xG"))

                form += xG.get("xG__sum")
                percentage += 1

        form /= percentage
        return form

    @property
    def xgc_form(self):
        form = 0.0
        percentage = 0
        for gameweek_number in range(1, 28):
            gameweek = Gameweek.objects.get(number=gameweek_number)
            matches = gameweek.matches.filter(
                Q(away_team=self) | Q(home_team=self)
            )
            for match in matches:
                base_qs = UnderlyingStat.objects.filter(
                    Q(match=match), ~Q(player__team=self))

                if not base_qs.exists():
                    continue

                form *= 15 / 17
                percentage *= 15 / 17

                xGC = base_qs.aggregate(Sum("xG"))

                form += xGC.get("xG__sum")
                percentage += 1

        form /= percentage
        return form

    objects = TeamManager()

    def __str__(self):
        return self.name
