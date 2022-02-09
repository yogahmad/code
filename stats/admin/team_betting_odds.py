from django.contrib import admin

from stats.models.team_betting_odds import TeamBettingOdd


@admin.register(TeamBettingOdd)
class TeamBettingOddAdmin(admin.ModelAdmin):
    pass
