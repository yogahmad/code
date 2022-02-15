from django.contrib import admin

from stats.models import UnderlyingStat


@admin.register(UnderlyingStat)
class UnderlyingStatAdmin(admin.ModelAdmin):
    list_display = ["player", "match", "minutes",
                    "xG", "xA", "shots", "key_passes"]
    search_fiels = ["player__first_name",
                    "player__last_name", "player__display_name", ]
