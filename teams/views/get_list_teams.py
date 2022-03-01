from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from teams.services.get_list_teams import GetListTeamService


class GetListTeamAPI(APIView):
    permission_classes = (AllowAny,)

    class ListTeamSerializer(serializers.Serializer):
        class TeamSerializer(serializers.Serializer):
            fpl_id = serializers.IntegerField()
            name = serializers.CharField()
            short_name = serializers.CharField()

        teams = serializers.ListField(child=TeamSerializer())

    def get(self, request: Request, **kwargs) -> Response:
        result = GetListTeamService.run(**request.GET.dict())
        return Response(self.ListTeamSerializer(result).data)
