from django.urls import path  # noqa

from players.views import GetListPlayerAPI
from players.views.get_player_detailed_data import GetPlayerDetailedDataAPI

players_urls = [
    path("", GetListPlayerAPI.as_view(), name="get-list-player-api"),
    path("<uuid:player_id>/", GetPlayerDetailedDataAPI.as_view(),
         name="get-player-detailed-data-api"),
]

urlpatterns = []
urlpatterns += players_urls
