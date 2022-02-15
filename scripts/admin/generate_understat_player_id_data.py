from django.contrib import admin

from scripts.models import GenerateUnderstatPlayerIdData
from scripts.services import GenerateUnderstatPlayerIdDataService


@admin.register(GenerateUnderstatPlayerIdData)
class GenerateUnderlyingStatDataAdmin(admin.ModelAdmin):
    list_display = ["created_at", "team", "understat_team_id"]
    ordering = ("-created_at",)

    def save_model(self, request, obj, *args, **kwargs):
        GenerateUnderstatPlayerIdDataService.run(obj)
        return super().save_model(request, obj, *args, **kwargs)
