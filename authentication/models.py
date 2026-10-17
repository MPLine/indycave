
from django.db import models


class DiscoveredDeveloper(models.Model):
    """
    Temporary search results.
    Admin can review, approve, or reject each result.
    """

    STATUS_CHOICES = [
        ("pending", "Pending Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    developer_name = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)

    platforms = models.JSONField(default=list, blank=True)

    website = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    source_name = models.CharField(max_length=100)
    source_url = models.URLField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    discovered_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-discovered_at"]
        verbose_name = "Discovered Developer"
        verbose_name_plural = "Discovered Developers"

    def __str__(self):
        return f"{self.game_name} - {self.developer_name}"


class VerifiedDeveloper(models.Model):
    """
    Permanently stored developer contacts approved by the admin.
    """

    developer_name = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)

    platforms = models.JSONField(default=list, blank=True)

    website = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    source_name = models.CharField(max_length=100)
    source_url = models.URLField()

    is_verified = models.BooleanField(default=True)

    email_sent = models.BooleanField(default=False)
    email_sent_at = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Verified Developer"
        verbose_name_plural = "Verified Developers"

    def __str__(self):
        return f"{self.game_name} - {self.developer_name}"
