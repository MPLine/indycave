
from django.conf import settings
from django.db import models


class DeveloperProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="developer_profile",
    )

    email = models.EmailField()
    phone = models.CharField(max_length=30)

    studio_name = models.CharField(
        max_length=150,
        blank=True,
    )

    facebook_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    reddit_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.studio_name or self.user.username
