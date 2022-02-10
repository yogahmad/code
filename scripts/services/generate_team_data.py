import requests
from django.db import transaction

from commons.runnable import Runnable
from scripts.constants import FPL_BOOTSTRAP_STATIC_API_URL
from scripts.serializers import TeamDataRequest
from teams.models import Team


class GenerateTeamDataService(Runnable):
    @classmethod
    @transaction.atomic
    def run(cls):
        res = requests.get(FPL_BOOTSTRAP_STATIC_API_URL)
        team_data_serializer = TeamDataRequest(data=res.json())
        team_data_serializer.is_valid(raise_exception=True)
        team_data = team_data_serializer.validated_data.get("teams")

        created_teams = []
        updated_teams = []
        for team in team_data:
            try:
                existing_team = Team.objects.get(name=team.get("name"))
                existing_team.fpl_id = team.get("id")
                existing_team.short_name = team.get("short_name")
                existing_team.strength_attack_home = team.get(
                    "strength_attack_home",
                )
                existing_team.strength_attack_away = team.get(
                    "strength_attack_away",
                )
                existing_team.strength_defence_home = team.get(
                    "strength_defence_home",
                )
                existing_team.strength_defence_away = team.get(
                    "strength_defence_away",
                )
                updated_teams.append(existing_team)
            except Team.DoesNotExist:
                new_team = Team(
                    fpl_id=team.get("id"),
                    name=team.get("name"),
                    short_name=team.get("short_name"),
                    strength_attack_home=team.get("strength_attack_home"),
                    strength_attack_away=team.get("strength_attack_away"),
                    strength_defence_home=team.get("strength_defence_home"),
                    strength_defence_away=team.get("strength_defence_away"),
                )
                created_teams.append(new_team)

        Team.objects.bulk_create(created_teams)
        Team.objects.bulk_update(
            updated_teams,
            [
                "fpl_id",
                "short_name",
                "strength_attack_home",
                "strength_attack_away",
                "strength_defence_home",
                "strength_defence_away",
            ],
        )
