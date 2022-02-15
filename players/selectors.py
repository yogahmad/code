from unidecode import unidecode

from players.models import Player
from teams.models import Team


class PlayerSelector:
    @classmethod
    def get_player_by_full_name_and_id(
        cls, full_name: str, id: int, team: Team
    ) -> Player:
        players = Player.objects.filter(understat_id=id)
        if players.exists():
            return players.first()

        all_players = Player.objects.filter(team=team).all()
        max_score = -1
        ret = None

        for player in all_players:
            if player.understat_id is not None:
                continue

            actual_name = player.first_name + " " + player.last_name
            score = cls._get_name_compatibility_score(
                full_name=full_name,
                actual_name=actual_name,
            )
            score_2 = cls._get_name_compatibility_score(
                full_name=full_name,
                actual_name=player.display_name,
            )
            score_3 = cls._get_name_compatibility_score(
                full_name=full_name,
                actual_name=player.last_name + " " + player.first_name,
            )

            if score_2 > score:
                score = score_2
            if score_3 > score:
                score = score_3

            if score > max_score:
                max_score = score
                ret = player

        return ret

    @classmethod
    def _get_name_compatibility_score(cls, full_name: str, actual_name: str) -> int:
        full_name = unidecode(full_name)
        full_name = "".join(ch for ch in full_name if ch.isalpha())
        full_name = full_name.lower()
        actual_name = unidecode(actual_name)
        actual_name = "".join(ch for ch in actual_name if ch.isalpha())
        actual_name = actual_name.lower()
        current_index = 0
        for ch in actual_name:
            if current_index < len(full_name) and full_name[current_index] == ch:
                current_index += 1
        return current_index
