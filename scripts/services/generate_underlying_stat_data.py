import json
from time import sleep

import requests
from django.db import transaction

from commons.runnable import Runnable
from matches.models import Match
from players.models import Player
from scripts.constants import UNDERSTAT_MATCH_API
from scripts.models.generate_underlying_stat_data import \
    GenerateUnderlyingStatData
from scripts.serializers.generate_underlying_stat_data import \
    UnderlyingStatDataRequest
from stats.models import UnderlyingStat
from teams.models import Team


class GenerateUnderlyingStatDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls, obj: GenerateUnderlyingStatData):
        ids = obj.ids.split(",")
        for id in ids:
            res = requests.get(UNDERSTAT_MATCH_API(id))
            sleep(2)
            data = res._content.decode("unicode-escape")
            data = cls._scrap_rosters_data(data)

            serializer = UnderlyingStatDataRequest(data=json.loads(data))
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            home_team = None
            away_team = None
            for player_id in data.get("h"):
                player_data = data.get("h").get(player_id)
                home_team = Team.objects.get(understat_id=player_data.get("team_id"))
                break
            for player_id in data.get("a"):
                player_data = data.get("a").get(player_id)
                away_team = Team.objects.get(understat_id=player_data.get("team_id"))
                break

            match = Match.objects.get(
                home_team=home_team,
                away_team=away_team,
            )

            for id in data.get("h"):
                player_data = data.get("h").get(id)
                player_id = player_data.get("player_id")
                xG = player_data.get("xG")
                xA = player_data.get("xA")
                shots = player_data.get("shots")
                key_passes = player_data.get("key_passes")
                minutes = player_data.get("time")
                try:
                    player = Player.objects.get(understat_id=player_id)
                except Player.DoesNotExist:
                    print(player_data)
                    continue

                if UnderlyingStat.objects.filter(
                    match=match,
                    player=player,
                ).exists():
                    continue

                stat = UnderlyingStat(
                    xG=xG,
                    xA=xA,
                    shots=shots,
                    key_passes=key_passes,
                    match=match,
                    player=player,
                    minutes=minutes,
                )
                stat.save()

            for id in data.get("a"):
                player_data = data.get("a").get(id)
                player_id = player_data.get("player_id")
                xG = player_data.get("xG")
                xA = player_data.get("xA")
                shots = player_data.get("shots")
                key_passes = player_data.get("key_passes")
                minutes = player_data.get("time")
                try:
                    player = Player.objects.get(understat_id=player_id)
                except Player.DoesNotExist:
                    print(player_data)
                    continue
                if UnderlyingStat.objects.filter(
                    match=match,
                    player=player,
                ).exists():
                    continue

                stat = UnderlyingStat(
                    xG=xG,
                    xA=xA,
                    shots=shots,
                    key_passes=key_passes,
                    match=match,
                    player=player,
                    minutes=minutes,
                )
                stat.save()

    @classmethod
    def _scrap_rosters_data(cls, data: str):
        index = data.find("rostersData")
        left = data.find("'", index) + 1
        right = data.find("'", left)
        return data[left:right]
