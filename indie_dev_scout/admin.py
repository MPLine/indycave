
from django.contrib import admin
from .models import DiscoveredDeveloper, VerifiedDeveloper


@admin.register(DiscoveredDeveloper)
class DiscoveredDeveloperAdmin(admin.ModelAdmin):
    list_display = (
        "game_name",
        "developer_name",
        "source_name",
        "status",
        "discovered_at",
    )

    list_filter = ("status", "source_name", "discovered_at")

    search_fields = (
        "game_name",
        "developer_name",
        "contact_email",
    )

    readonly_fields = ("discovered_at", "reviewed_at")

    ordering = ("-discovered_at",)


@admin.register(VerifiedDeveloper)
class VerifiedDeveloperAdmin(admin.ModelAdmin):
    list_display = (
        "game_name",
        "developer_name",
        "contact_email",
        "is_verified",
        "email_sent",
        "created_at",
    )

    list_filter = ("is_verified", "email_sent", "created_at")

    search_fields = (
        "game_name",
        "developer_name",
        "contact_email",
    )

    readonly_fields = ("created_at", "updated_at", "email_sent_at")

    ordering = ("-created_at",)
