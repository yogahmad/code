from django.urls import path  # noqa

from gameweeks.views import ListGameweekDataAPI

players_urls = [
    path("", ListGameweekDataAPI.as_view(), name="list-gameweek-data-api"),
]

urlpatterns = []
urlpatterns += players_urls
