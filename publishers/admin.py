from django.contrib import admin
from .models import Publisher
# Register your models here.


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "game_types_focus",
        "platforms",
        "official_website",
    )

    search_fields = (
        "name",
        "game_types_focus",
        "platforms",
    )