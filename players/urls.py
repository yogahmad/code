from django.urls import path  # noqa

from players.views import GetListPlayerAPI

players_urls = [
    path("", GetListPlayerAPI.as_view(), name="get-list-player-api"),
]

urlpatterns = []
urlpatterns += players_urls
