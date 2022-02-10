import requests
from django.db import transaction

from commons.runnable import Runnable
from players.models import Player
from scripts.constants import FPL_BOOTSTRAP_STATIC_API_URL
from scripts.serializers import PlayerDataRequest
from teams.models import Team


class GeneratePlayerDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls):
        res = requests.get(FPL_BOOTSTRAP_STATIC_API_URL)
        player_data_serializer = PlayerDataRequest(data=res.json())
        player_data_serializer.is_valid(raise_exception=True)
        player_data = player_data_serializer.validated_data.get("elements")

        updated_players = []
        created_players = []
        for player in player_data:
            team = Team.objects.get(fpl_id=player.get("team"))

            try:
                existing_player: Player = Player.objects.get(
                    fpl_id=player.get("id"),
                )
                existing_player.first_name = player.get("first_name")
                existing_player.last_name = player.get("second_name")
                existing_player.display_name = player.get("web_name")
                existing_player.price = player.get("now_cost")
                existing_player.photo_id = player.get("photo")
                existing_player.chance_of_playing_this_round = player.get(
                    "chance_of_playing_this_round"
                )
                existing_player.chance_of_playing_next_round = player.get(
                    "chance_of_playing_next_round"
                )
                existing_player.team = team
                existing_player.position = player.get("element_type")

                updated_players.append(existing_player)
            except Player.DoesNotExist:
                new_player = Player(
                    fpl_id=player.get("id"),
                    first_name=player.get("first_name"),
                    last_name=player.get("second_name"),
                    display_name=player.get("web_name"),
                    price=player.get("now_cost"),
                    photo_id=player.get("photo"),
                    chance_of_playing_this_round=player.get(
                        "chance_of_playing_this_round"
                    ),
                    chance_of_playing_next_round=player.get(
                        "chance_of_playing_next_round"
                    ),
                    team=team,
                    position=player.get("element_type"),
                )
                created_players.append(new_player)

        Player.objects.bulk_create(created_players)
        Player.objects.bulk_update(
            updated_players,
            [
                "first_name",
                "last_name",
                "display_name",
                "price",
                "photo_id",
                "chance_of_playing_this_round",
                "chance_of_playing_next_round",
                "team",
                "position",
            ],
        )
