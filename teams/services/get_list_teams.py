from collections import namedtuple
from dataclasses import dataclass
from typing import List, Optional

from django.db.models import Q
from django.db.models.functions import Lower

from commons.runnable import Runnable
from teams.models import Team


@dataclass
class TeamDataclass:
    fpl_id: int
    name: str
    short_name: str


@dataclass
class ListTeamDataclass:
    teams: List[TeamDataclass]


class GetListTeamService(Runnable):
    @classmethod
    def run(cls) -> ListTeamDataclass:
        base_queryset = Team.objects.all().order_by("name")
        teams = [
            TeamDataclass(
                fpl_id=team.fpl_id,
                name=team.name,
                short_name=team.short_name
            )
            for team in base_queryset
        ]

        return ListTeamDataclass(
            teams=teams,
        )
