from django.contrib import admin

from scripts.models import GenerateTeamData
from scripts.services.generate_team_data import GenerateTeamDataService


@admin.register(GenerateTeamData)
class GenerateTeamDataAdmin(admin.ModelAdmin):
    list_display = ["created_at"]

    def save_model(self, request, obj, *args, **kwargs):
        GenerateTeamDataService.run()
        return super().save_model(request, obj, *args, **kwargs)
