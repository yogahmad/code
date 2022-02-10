from django.contrib import admin
from stats.models.shots_data import ShotsData


@admin.register(ShotsData)
class ShotsDataAdmin(admin.ModelAdmin):
    pass
