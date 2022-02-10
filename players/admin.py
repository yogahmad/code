from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["__str__", "team", "position"]
    list_filter = ["team", "position"]
    ordering = ["__str__"]
