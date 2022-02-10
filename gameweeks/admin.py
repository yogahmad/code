from django.contrib import admin

from gameweeks.models import Gameweek


@admin.register(Gameweek)
class GameweekAdmin(admin.ModelAdmin):
    list_display = ["gameweek_number_display"]
    ordering = ["number"]

    def gameweek_number_display(self, obj):
        return "Gameweek {}".format(obj.number)

    gameweek_number_display.short_description = "Gameweek"
