from dataclasses import dataclass
from typing import List, Optional

from django.db.models import Q

from commons.runnable import Runnable
from players.models import Player


@dataclass
class PlayerDataclass:
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


@dataclass
class ListPlayerDataclass:
    players: List[PlayerDataclass]


class GetListPlayerService(Runnable):
    @classmethod
    def run(
        cls,
        position: Optional[int] = None,
        team_ids: Optional[List[int]] = None,
        player_name: Optional[str] = None,
        **kwargs
    ) -> ListPlayerDataclass:
        query = Q()
        if position:
            query = query & Q(position=position)
        if team_ids:
            query = query & Q(team__fpl_id__in=team_ids)
        if player_name:
            query = query & (
                Q(first_name__icontains=player_name)
                | Q(last_name__icontains=player_name)
                | Q(display_name__icontains=player_name)
            )

        players = Player.objects.filter(query).order_by("-price")

        all_players = []
        for player in players:
            all_players.append(
                PlayerDataclass(
                    fpl_id=player.fpl_id,
                    full_name=player.first_name + ' ' + player.last_name,
                    display_name=player.display_name,
                    price=player.price,
                    photo_id=player.photo_id,
                    chance_of_playing_this_round=player.chance_of_playing_this_round,
                    chance_of_playing_next_round=player.chance_of_playing_next_round,
                    position=Player.POSITION_TYPE_CHOICES.get(player.position),
                    understat_id=player.understat_id,
                    team=player.team.name,
                    team_id=player.team.fpl_id,
                )
            )

        return ListPlayerDataclass(players=all_players)
