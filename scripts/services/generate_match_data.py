import requests
from django.db import transaction

from commons.runnable import Runnable
from gameweeks.models import Gameweek
from scripts.constants import FPL_MATCH_API_URL
from scripts.models import GenerateGameweekData


class GenerateMatchDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls):
        res = requests.get(FPL_MATCH_API_URL)
        print(res)
