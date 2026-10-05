from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)

    game_types_focus = models.TextField(blank=True)

    platforms = models.TextField(blank=True)

    public_pitch_contact = models.TextField(blank=True)

    official_website = models.URLField(blank=True)

    def __str__(self):
        return self.name