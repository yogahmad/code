from django.contrib import admin

from gameweeks.models import Gameweek


@admin.register(Gameweek)
class GameweekAdmin(admin.ModelAdmin):
    pass
