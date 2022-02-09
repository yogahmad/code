from django.contrib import admin

from stats.models.previous_season_total_points import PreviousSeasonTotalPoint


@admin.register(PreviousSeasonTotalPoint)
class PreviousSeasonTotalPointAdmin(admin.ModelAdmin):
    pass
