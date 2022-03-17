from dataclasses import dataclass
from math import ceil, floor
from typing import List, Optional

from django.db.models import Sum
from django.db.models.functions import Coalesce

from commons.runnable import Runnable
from players.models import Player
from stats.models.points import Point


@dataclass
class PlayerDetailedDataclass:
    fpl_id: int
    full_name: str
    display_name: str
    price: int
    photo_id: str
    chance_of_playing_this_round: int
    chance_of_playing_next_round: int
    position: str
    understat_id: Optional[int]
    team: str
    team_id: int


class GetPlayerDetailedDataService(Runnable):
    @classmethod
    def run(
        cls,
        player_id,
        **kwargs
    ) -> PlayerDetailedDataclass:
        player: Player = Player.objects.get(id=player_id)
        points = player.points
        matches = points.values("match").order_by(
            "-match__gameweek__number").distinct()
        result = []
        for match in matches.iterator():
            minutes = (
                points.filter(
                    identifier=Point.PointType.MINUTES,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            goal_scored = (
                points.filter(
                    identifier=Point.PointType.GOALS_SCORED,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            assists = (
                points.filter(
                    identifier=Point.PointType.ASSISTS,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            clean_sheets = (
                points.filter(
                    identifier=Point.PointType.CLEAN_SHEETS,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            goal_conceded = (
                points.filter(
                    identifier=Point.PointType.GOALS_CONCEDED,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            own_goals = (
                points.filter(
                    identifier=Point.PointType.OWN_GOALS,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            penalties_saved = (
                points.filter(
                    identifier=Point.PointType.PENALTIES_SAVED,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            penalties_missed = (
                points.filter(
                    identifier=Point.PointType.PENALTIES_MISSED,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            yellow_cards = (
                points.filter(
                    identifier=Point.PointType.YELLOW_CARDS,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            red_cards = (
                points.filter(
                    identifier=Point.PointType.RED_CARDS,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            saves = (
                points.filter(
                    identifier=Point.PointType.SAVES,
                    match__id=match["match"],
                ).aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]
            bonus = (
                points.filter(
                    identifier=Point.PointType.BONUS,
                    match__id=match["match"],
                )
                .aggregate(number=Coalesce(Sum("number"), 0))
            )["number"]

            total_points = 0
            if minutes > 60:
                total_points += 2
            elif minutes > 0:
                total_points += 1

            if player.position == Player.PositionType.FWD:
                total_points += goal_scored * 4
            elif player.position == Player.PositionType.MID:
                total_points += goal_scored * 5
            else:
                total_points += goal_scored * 6

            total_points += assists * 3

            if player.position == Player.PositionType.FWD:
                total_points += clean_sheets * 0
            elif player.position == Player.PositionType.MID:
                total_points += clean_sheets * 1
            else:
                total_points += clean_sheets * 4

            if (player.position == Player.PositionType.GK or player.PositionType.DEF):
                total_points -= floor(goal_conceded / 2)

            total_points -= own_goals * 2

            total_points += penalties_saved * 5

            total_points -= penalties_missed * 2

            total_points -= yellow_cards * 1

            total_points -= red_cards * 3

            total_points += ceil(saves / 3)

            total_points += bonus

            result.append(total_points)

        return result
