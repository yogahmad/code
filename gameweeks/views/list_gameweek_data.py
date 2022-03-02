from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gameweeks.services import ListGameweekDataService


class ListGameweekDataAPI(APIView):
    permission_classes = (AllowAny,)

    class ListGameweekSerializer(serializers.Serializer):
        class GameweekSerializer(serializers.Serializer):
            class MatchSerializer(serializers.Serializer):
                fpl_id = serializers.IntegerField()
                away_team_name = serializers.CharField()
                away_team_fpl_id = serializers.IntegerField()
                away_team_xg_form = serializers.FloatField()
                away_team_xgc_form = serializers.FloatField()
                away_defence_color = serializers.IntegerField()
                away_attack_color = serializers.IntegerField()
                home_team_name = serializers.CharField()
                home_team_fpl_id = serializers.IntegerField()
                home_team_xg_form = serializers.FloatField()
                home_team_xgc_form = serializers.FloatField()
                home_defence_color = serializers.IntegerField()
                home_attack_color = serializers.IntegerField()

            number = serializers.IntegerField()
            matches = serializers.ListField(child=MatchSerializer())

        gameweeks = serializers.ListField(child=GameweekSerializer())

    def get(self, request: Request, **kwargs) -> Response:
        result = ListGameweekDataService.run()
        return Response(self.ListGameweekSerializer(result).data)
