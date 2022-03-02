from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from gameweeks.services import ListGameweekDataService


class ListGameweekDataAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, **kwargs) -> Response:
        result = ListGameweekDataService.run()
        return Response()
