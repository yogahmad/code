import requests
from django.db import transaction

from commons.runnable import Runnable
from matches.models import Match
from players.models import Player
from scripts.constants import (FPL_PLAYERS_POINT_API_URL,
                               FPL_PLAYERS_POINT_BY_GAMEWEEK_API_URL)
from scripts.models import GeneratePlayersPointData
from scripts.serializers import (PlayersPointDataByGameweekRequest,
                                 PlayersPointDataRequest)
from stats.models import Point


class GeneratePlayersPointDataService(Runnable):
    @classmethod
    def run(cls, generate_data: GeneratePlayersPointData):
        if generate_data.team:
            players = Player.objects.filter(
                team=generate_data.team,
            ).all()
            for player in players:
                with transaction.atomic():
                    res = requests.get(
                        FPL_PLAYERS_POINT_API_URL(player.fpl_id),
                    )
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
        elif generate_data.gameweek:
            res = requests.get(
                FPL_PLAYERS_POINT_BY_GAMEWEEK_API_URL(
                    generate_data.gameweek.number,
                )
            )
            serializer = PlayersPointDataByGameweekRequest(data=res.json())
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

            for element in data.get("elements"):
                player_id = element.get("id")
                player = Player.objects.get(fpl_id=player_id)
                for stats in element.get("explain"):
                    fixture_id = stats.get("fixture")
                    match = Match.objects.get(fpl_id=fixture_id)
                    for stat in stats.get("stats"):
                        identifier = stat.get("identifier")
                        value = stat.get("value")

                        point_data, _ = Point.objects.get_or_create(
                            identifier=identifier,
                            player=player,
                            match=match,
                        )
                        point_data.number = value
                        point_data.save()
        else:
            for gameweek in range(1, 39):
                res = requests.get(
                    FPL_PLAYERS_POINT_BY_GAMEWEEK_API_URL(
                        gameweek,
                    )
                )
                serializer = PlayersPointDataByGameweekRequest(data=res.json())
                serializer.is_valid(raise_exception=True)
                data = serializer.validated_data

                for element in data.get("elements"):
                    player_id = element.get("id")
                    player = Player.objects.get(fpl_id=player_id)
                    for stats in element.get("explain"):
                        fixture_id = stats.get("fixture")
                        match = Match.objects.get(fpl_id=fixture_id)
                        for stat in stats.get("stats"):
                            identifier = stat.get("identifier")
                            value = stat.get("value")

                            point_data, _ = Point.objects.get_or_create(
                                identifier=identifier,
                                player=player,
                                match=match,
                            )
                            point_data.number = value
                            point_data.save()
