from django.contrib import admin

from stats.models.shots_conceded_data import ShotsConcededData


@admin.register(ShotsConcededData)
class ShotsConcededDataAdmin(admin.ModelAdmin):
    pass
