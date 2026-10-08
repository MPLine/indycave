from django.db import models


class Publisher(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True
    )

    game_types_focus = models.TextField(
        blank=True
    )

    platforms = models.TextField(
        blank=True
    )

    pitch_url = models.URLField(
        blank=True
    )

    pitch_email = models.EmailField(
        blank=True
    )

    pitch_requirements = models.TextField(
        blank=True
    )

    official_website = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.name