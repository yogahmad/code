from django.contrib import admin

from scripts.models import GeneratePlayersPointData
from scripts.services import GeneratePlayersPointDataService


@admin.register(GeneratePlayersPointData)
class GeneratePlayerDataAdmin(admin.ModelAdmin):
    list_display = ["team", "created_at"]
    ordering = ("created_at", "team")

    def save_model(self, request, obj, *args, **kwargs):
        GeneratePlayersPointDataService.run(obj)
        return super().save_model(request, obj, *args, **kwargs)
