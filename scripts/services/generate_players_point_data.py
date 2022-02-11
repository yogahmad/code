import requests
from django.db import transaction

from commons.runnable import Runnable
from players.models import Player
from scripts.constants import FPL_PLAYERS_POINT_API_URL, FPL_PLAYERS_POINT_BY_GAMEWEEKAPI_URL
from scripts.serializers import PlayersPointDataRequest
from teams.models import Team
from stats.models import Point
from matches.models import Match
from scripts.models import GeneratePlayersPointData


class GeneratePlayersPointDataService(Runnable):
    @classmethod
    def run(cls, generate_data: GeneratePlayersPointData):
        if hasattr(generate_data, "team"):
            players = Player.objects.filter(
                team=generate_data.team,
            ).all()
            for player in players:
                with transaction.atomic():
                    res = requests.get(
                        FPL_PLAYERS_POINT_API_URL(player.fpl_id))
                    serializer = PlayersPointDataRequest(data=res.json())
                    serializer.is_valid(raise_exception=True)
                    data = serializer.validated_data

                    for result in data.get("history"):
                        match = Match.objects.get(fpl_id=result.get("fixture"))
                        for key in Point.POINT_TYPE_CHOICES.keys():
                            point_data, created = Point.objects.get_or_create(
                                identifier=key,
                                player=player,
                                match=match,
                            )
                            point_data.number = result.get(key)
                            point_data.save()
        elif hasattr(generate_data, "gameweek"):
            res = requests.get(FPL_PLAYERS_POINT_BY_GAMEWEEKAPI_URL(
                generate_data.gameweek.number))
