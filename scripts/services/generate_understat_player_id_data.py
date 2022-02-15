import json

import requests
from django.db import transaction
from rest_framework import serializers

from commons.runnable import Runnable
from players.selectors import PlayerSelector
from scripts.constants import UNDERSTAT_TEAM_API
from scripts.models import GenerateUnderstatPlayerIdData


class _DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    player_name = serializers.CharField()


class GenerateUnderstatPlayerIdDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls, obj: GenerateUnderstatPlayerIdData):
        res = requests.get(UNDERSTAT_TEAM_API(obj.understat_team_id))
        data = res._content.decode("unicode-escape")
        data = cls._scrap_rosters_data(data)
        data = json.loads(data)

        for player_data in data:
            serializer = _DataSerializer(data=player_data)
            serializer.is_valid(raise_exception=True)
            player_data = serializer.validated_data

            player = PlayerSelector.get_player_by_full_name_and_id(
                full_name=player_data.get("player_name"),
                id=player_data.get("id"),
                team=obj.team,
            )

            player.understat_id = player_data.get("id")
            player.save()

    @classmethod
    def _scrap_rosters_data(cls, data: str):
        index = data.find("playersData")
        left = data.find("'", index) + 1
        right = data.find("'", left)
        return data[left:right]
