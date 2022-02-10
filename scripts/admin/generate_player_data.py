from django.contrib import admin

from scripts.models import GeneratePlayerData
from scripts.services import GeneratePlayerDataService


@admin.register(GeneratePlayerData)
class GeneratePlayerDataAdmin(admin.ModelAdmin):
    list_display = ["created_at"]

    def save_model(self, request, obj, *args, **kwargs):
        GeneratePlayerDataService.run()
        return super().save_model(request, obj, *args, **kwargs)
