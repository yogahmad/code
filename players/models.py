from django.db import models

from commons.models import BaseModel


class PlayerManager(models.Manager):
    pass


class Player(BaseModel):
    class ChanceOfPlayingType:
        GREEN = 100
        YELLOW = 75
        ORANGE = 50
        AMBER = 25
        RED = 0

    class PositionType:
        GK = 1
        DEF = 2
        MID = 3
        FWD = 4

    CHANCE_OF_PLAYING_TYPE_CHOICES = {
        ChanceOfPlayingType.GREEN: 100,
        ChanceOfPlayingType.YELLOW: 75,
        ChanceOfPlayingType.ORANGE: 50,
        ChanceOfPlayingType.AMBER: 25,
        ChanceOfPlayingType.GREEN: 0,
    }

    POSITION_TYPE_CHOICES = {
        PositionType.GK: "Goalkeeper",
        PositionType.DEF: "Defender",
        PositionType.MID: "Midfielder",
        PositionType.FWD: "Forward",
    }

    fpl_id = models.IntegerField(blank=False, null=False, unique=True)
    first_name = models.CharField(blank=False, null=False, max_length=128)
    last_name = models.CharField(blank=False, null=False, max_length=128)
    display_name = models.CharField(blank=False, null=False, max_length=128)
    price = models.IntegerField(blank=False, null=False)
    photo_id = models.CharField(blank=False, null=False, max_length=32)
    chance_of_playing_this_round = models.IntegerField(
        blank=True,
        null=True,
        choices=CHANCE_OF_PLAYING_TYPE_CHOICES.items(),
        default=ChanceOfPlayingType.GREEN,
    )
    chance_of_playing_next_round = models.IntegerField(
        blank=True,
        null=True,
        choices=CHANCE_OF_PLAYING_TYPE_CHOICES.items(),
    )
    team = models.ForeignKey(
        "teams.Team",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="players",
    )
    position = models.IntegerField(
        blank=False,
        null=False,
        choices=POSITION_TYPE_CHOICES.items(),
    )

    objects = PlayerManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
