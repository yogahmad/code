import requests
from django.db import transaction
from django.db.models import Q

from commons.runnable import Runnable
from gameweeks.models import Gameweek
from matches.models import Match
from scripts.constants import FPL_MATCH_API_URL
from scripts.serializers.match_data_serializer import MatchDataSerializer
from teams.models import Team


class GenerateMatchDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls):
        res = requests.get(FPL_MATCH_API_URL)
        matches = res.json()

        created_match = []
        updated_match = []
        for match in matches:
            match_data_serializer = MatchDataSerializer(data=match)
            match_data_serializer.is_valid(raise_exception=True)
            match_data = match_data_serializer.validated_data

            home_team_fpl_id = match_data.get("team_h")
            away_team_fpl_id = match_data.get("team_a")
            fpl_id = match_data.get("id")

            gameweek_number = match_data.get("event", None)
            gameweek = None
            if gameweek_number:
                gameweek = Gameweek.objects.get(number=gameweek_number)

            try:
                existing_match = Match.objects.get(
                    Q(home_team__fpl_id=home_team_fpl_id),
                    Q(away_team__fpl_id=away_team_fpl_id),
                )
                existing_match.fpl_id = fpl_id
                existing_match.gameweek = gameweek
                updated_match.append(existing_match)
            except Match.DoesNotExist:
                home_team = Team.objects.get(fpl_id=home_team_fpl_id)
                away_team = Team.objects.get(fpl_id=away_team_fpl_id)

                new_match = Match(
                    fpl_id=fpl_id,
                    home_team=home_team,
                    away_team=away_team,
                    gameweek=gameweek,
                )
                created_match.append(new_match)

        Match.objects.bulk_create(created_match)
        Match.objects.bulk_update(updated_match, ["fpl_id", "gameweek"])
