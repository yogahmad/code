from django.contrib import admin

from scripts.models import GenerateMatchData
from scripts.services.generate_match_data import GenerateMatchDataService


@admin.register(GenerateMatchData)
class GenerateMatchDataAdmin(admin.ModelAdmin):
    list_display = ["created_at"]

    def save_model(self, request, obj, *args, **kwargs):
        GenerateMatchDataService.run()
        return super().save_model(request, obj, *args, **kwargs)
