from django.contrib import admin

from scripts.models import GenerateGameweekData
from scripts.services import GenerateGameweekDataService


@admin.register(GenerateGameweekData)
class GenerateGameweekDataAdmin(admin.ModelAdmin):
    list_display = [
        "start_gameweek",
        "end_gameweek",
        "created_at",
    ]
    list_display_links = None

    def save_model(self, request, obj, *args, **kwargs):
        GenerateGameweekDataService.run(generateGameweekData=obj)
        return super().save_model(request, obj, *args, **kwargs)
