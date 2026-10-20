
from django.conf import settings
from django.db import models


class Game(models.Model):

    GENRE_CHOICES = [
        ("action", "Action"),
        ("adventure", "Adventure"),
        ("racing", "Racing"),
        ("horror", "Horror"),
        ("fps", "FPS"),
        ("rpg", "RPG"),
        ("strategy", "Strategy"),
        ("simulation", "Simulation"),
        ("sports", "Sports"),
        ("platformer", "Platformer"),
        ("puzzle", "Puzzle"),
        ("survival", "Survival"),
        ("educatif","Educatif")
    
    ]

    PLATFORM_CHOICES = [
        ("pc", "PC"),
        ("playstation", "PlayStation"),
        ("xbox", "Xbox"),
        ("nintendo", "Nintendo"),
        ("mobile", "Mobile"),
        ("web", "Web"),
    ]

    DEVELOPMENT_STAGE_CHOICES = [
        ("concept", "Concept"),
        ("prototype", "Prototype"),
        ("early_development", "Early Development"),
        ("in_development", "In Development"),
        ("playable_demo", "Playable Demo"),
        ("early_access", "Early Access"),
        ("completed", "Completed"),
    ]
    
    PUBLISHER_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("publisher_list_ready", "Publisher List Ready"),
    ]

    developer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="games",
    )

    title = models.CharField(max_length=200)
    short_description = models.TextField()
    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
    )
    platforms = models.JSONField(default=list)
    development_stage = models.CharField(
        max_length=30,
        choices=DEVELOPMENT_STAGE_CHOICES,
    )

    official_page_url = models.URLField(blank=True)
    gameplay_demo_url = models.URLField(blank=True)
    cover_image = models.ImageField(
        upload_to="static/images/game_covers/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    publisher_status = models.CharField(
        max_length=30,
        choices=PUBLISHER_STATUS_CHOICES,
        default="pending",
    )


    def __str__(self):
        return self.title


class GamePublisherMatch(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("sent", "Sent"),
    ]

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="publisher_matches",
    )

    publisher = models.ForeignKey(
        "publishers.Publisher",
        on_delete=models.CASCADE,
        related_name="game_matches",
    )

    match_score = models.PositiveSmallIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("game", "publisher")
        ordering = ["-match_score"]

    def __str__(self):
        return f"{self.game.title} - {self.publisher.name}"
