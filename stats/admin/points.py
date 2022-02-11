from django.contrib import admin

from stats.models.points import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):

    list_display = ["player", "identifier", "number", "match"]
    list_filter = ["identifier", "player", "player__team"]
    ordering = ("-number"),
    list_select_related = ["player"]
    search_fields = ("player__display_name"),
