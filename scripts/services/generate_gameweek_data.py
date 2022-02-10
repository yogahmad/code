from django.db import transaction

from commons.runnable import Runnable
from gameweeks.models import Gameweek
from scripts.models import GenerateGameweekData


class GenerateGameweekDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls, generateGameweekData: GenerateGameweekData):
        gameweeks = []
        for number in range(
            generateGameweekData.start_gameweek,
            generateGameweekData.end_gameweek + 1,
        ):
            new_gameweek = Gameweek(number=number)
            gameweeks.append(new_gameweek)
        Gameweek.objects.bulk_create(gameweeks)
