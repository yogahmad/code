from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from players.services.get_list_player import GetListPlayerService


class GetListPlayerAPI(APIView):
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

    def get(self, request: Request, **kwargs) -> Response:
        result = GetListPlayerService.run(**request.GET.dict())
        return Response(self.ListPlayerSerializer(result).data)
