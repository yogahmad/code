from django.urls import path  # noqa

from teams.views.get_list_teams import GetListTeamAPI

players_urls = [
    path("", GetListTeamAPI.as_view(), name="get-list-team-api"),
]

urlpatterns = []
urlpatterns += players_urls
