from django.contrib import admin

from matches.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["match_display_name", "gameweek_number_display", ]
    list_filter = ["gameweek", "home_team", "away_team", ]
    ordering = ["gameweek__number"]

    def match_display_name(self, obj):
        return "{} vs {}".format(obj.home_team.name, obj.away_team.name)

    match_display_name.short_description = "Match"

    def gameweek_number_display(self, obj):
        if obj.gameweek:
            return "Gameweek {}".format(obj.gameweek.number)
        return "Postponed"

    gameweek_number_display.short_description = "Gameweek"
