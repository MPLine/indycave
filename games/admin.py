
from django.contrib import admin, messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import path, reverse
from django.utils.html import format_html

from .models import Game, GamePublisherMatch


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "developer",
        "genre",
        "development_stage",
        "publisher_status",
        "created_at",
    )

    list_filter = (
        "genre",
        "development_stage",
        "publisher_status",
        "created_at",
    )

    search_fields = (
        "title",
        "developer__username",
        "developer__email",
    )

    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    list_per_page = 25


@admin.register(GamePublisherMatch)
class GamePublisherMatchAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "publisher",
        "match_score",
        "status",
        "visit_website_button",
        "send_to_developer_button",
        "created_at",
    )

    list_filter = ("status", "created_at")
    search_fields = ("game__title", "publisher__name")
    ordering = ("-match_score",)
    list_per_page = 25

    def visit_website_button(self, obj):
        url = obj.publisher.official_website

        if not url:
            return "No website"

        return format_html(
            '<a class="button" href="{}" target="_blank" '
            'rel="noopener noreferrer">Visit Website</a>',
            url,
        )

    visit_website_button.short_description = "Website"

    def send_to_developer_button(self, obj):
        if obj.status == "sent":
            return "Already sent"

        url = reverse(
            "admin:games_gamepublishermatch_send",
            args=[obj.pk],
        )

        return format_html(
            '<a class="button" href="{}">Send to Developer</a>',
            url,
        )

    send_to_developer_button.short_description = "Send"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                "<int:match_id>/send-to-developer/",
                self.admin_site.admin_view(self.send_to_developer),
                name="games_gamepublishermatch_send",
            ),
        ]

        return custom_urls + urls

    def send_to_developer(self, request, match_id):
        match = get_object_or_404(
            GamePublisherMatch,
            pk=match_id,
        )

        if match.status != "sent":
            match.status = "sent"
            match.save(update_fields=["status", "updated_at"])

            match.game.publisher_status = "publisher_list_ready"
            match.game.save(update_fields=["publisher_status"])

            self.message_user(
                request,
                f"{match.publisher.name} was sent to the developer "
                f"for {match.game.title}.",
                level=messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "This publisher has already been sent.",
                level=messages.WARNING,
            )

        return redirect(
            reverse("admin:games_gamepublishermatch_changelist")
        )
