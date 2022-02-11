from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["__str__", "team", "position", "fpl_id"]
    list_filter = ["team", "position"]
    ordering = ["team__name", "position", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
