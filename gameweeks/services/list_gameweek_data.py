from dataclasses import dataclass
from typing import List, Optional

from django.db.models import Q

from commons.runnable import Runnable
from gameweeks.models import Gameweek
from teams.models import Team


@dataclass
class MatchDataclass:
    fpl_id: int
    away_team_name: str
    away_team_fpl_id: int
    away_team_xg_form: float
    away_team_xgc_form: float
    away_defence_color: int
    away_attack_color: int
    home_team_name: str
    home_team_fpl_id: int
    home_team_xg_form: float
    home_team_xgc_form: float
    home_defence_color: int
    home_attack_color: int


@dataclass
class GameweekDataclass:
    number: int
    matches: List[MatchDataclass]


@dataclass
class ListGameweekDataclass:
    gameweeks: List[GameweekDataclass]


class ListGameweekDataService(Runnable):
    @classmethod
    def run(
        cls,
        next_n_gameweek: Optional[int] = None,
    ):
        base_qs = Gameweek.objects.prefetch_related().filter(
            ~Q(number=None)).all().prefetch_related("matches")

        teams_xg_form = {}
        teams_xgc_form = {}
        for team in Team.objects.all():
            teams_xg_form[team.fpl_id] = team.xg_form
            teams_xgc_form[team.fpl_id] = team.xgc_form

        min_xg_form = 100.0
        max_xg_form = 0.0
        min_xgc_form = 100.0
        max_xgc_form = 0.0

        for team in Team.objects.all():
            xg_form = teams_xg_form[team.fpl_id]
            xgc_form = teams_xgc_form[team.fpl_id]
            if xg_form > max_xg_form:
                max_xg_form = xg_form
            if xg_form < min_xg_form:
                min_xg_form = xg_form
            if xgc_form > max_xgc_form:
                max_xgc_form = xgc_form
            if xgc_form < min_xgc_form:
                min_xgc_form = xgc_form

        team_defence_color = {}
        team_attack_color = {}
        for team in Team.objects.all():
            xg_form = teams_xg_form[team.fpl_id]
            xgc_form = teams_xgc_form[team.fpl_id]
            xg_red_color = 0x00 + round((0xFF - 0x00) * (xg_form -
                                                         min_xg_form) / (max_xg_form - min_xg_form))
            xg_green_color = 0x00 + round((0xFF - 0x00) * (max_xg_form -
                                                           xg_form) / (max_xg_form - min_xg_form))

            xg_color = xg_red_color * 0x10000 + xg_green_color * 0x100 + 0xFF000000

            xgc_red_color = 0x00 + round((0xFF - 0x00) * (max_xgc_form -
                                                          xgc_form) / (max_xgc_form - min_xgc_form))
            xgc_green_color = 0x00 + round((0xFF - 0x00) * (xgc_form -
                                                            min_xgc_form) / (max_xgc_form - min_xgc_form))

            xgc_color = xgc_red_color * 0x10000 + xgc_green_color * 0x100 + 0xFF000000

            team_attack_color[team.fpl_id] = xg_color
            team_defence_color[team.fpl_id] = xgc_color

        gameweeks = []
        for gameweek in base_qs:
            matches = []
            for match in gameweek.matches.all():
                matches.append(
                    MatchDataclass(
                        fpl_id=match.fpl_id,
                        away_team_name=match.away_team.short_name,
                        away_team_fpl_id=match.away_team.fpl_id,
                        away_team_xg_form=teams_xg_form[match.away_team.fpl_id],
                        away_team_xgc_form=teams_xgc_form[match.away_team.fpl_id],
                        away_defence_color=team_defence_color[match.away_team.fpl_id],
                        away_attack_color=team_attack_color[match.away_team.fpl_id],
                        home_team_name=match.home_team.short_name,
                        home_team_fpl_id=match.home_team.fpl_id,
                        home_team_xg_form=teams_xg_form[match.home_team.fpl_id],
                        home_team_xgc_form=teams_xgc_form[match.home_team.fpl_id],
                        home_defence_color=team_defence_color[match.home_team.fpl_id],
                        home_attack_color=team_attack_color[match.home_team.fpl_id],
                    )
                )
            gameweeks.append(
                GameweekDataclass(
                    number=gameweek.number,
                    matches=matches,
                )
            )

        return ListGameweekDataclass(gameweeks=gameweeks)
