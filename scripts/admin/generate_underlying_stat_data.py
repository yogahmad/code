from django.contrib import admin

from scripts.models import GenerateUnderlyingStatData
from scripts.services import GenerateUnderlyingStatDataService


@admin.register(GenerateUnderlyingStatData)
class GenerateUnderlyingStatDataAdmin(admin.ModelAdmin):
    list_display = ["ids", "created_at"]
    ordering = ("-created_at",)

    def save_model(self, request, obj, *args, **kwargs):
        GenerateUnderlyingStatDataService.run(obj)
        return super().save_model(request, obj, *args, **kwargs)
