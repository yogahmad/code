from uuid import UUID
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from players.services.get_list_player import GetListPlayerService
from players.services.get_player_detailed_data import GetPlayerDetailedDataService


class GetPlayerDetailedDataAPI(APIView):
    permission_classes = (AllowAny,)

    class ListPlayerSerializer(serializers.Serializer):
        class PlayerSerializer(serializers.Serializer):
            fpl_id = serializers.IntegerField()
            full_name = serializers.CharField()
            display_name = serializers.CharField()
            price = serializers.IntegerField()
            photo_id = serializers.CharField()
            chance_of_playing_this_round = serializers.IntegerField()
            chance_of_playing_next_round = serializers.IntegerField()
            position = serializers.CharField()
            understat_id = serializers.IntegerField(allow_null=True)
            team = serializers.CharField()
            team_id = serializers.IntegerField()

        players = serializers.ListField(child=PlayerSerializer())

    def get(self, request: Request, player_id: UUID, **kwargs) -> Response:
        result = GetPlayerDetailedDataService.run(player_id=player_id)
        return Response()
