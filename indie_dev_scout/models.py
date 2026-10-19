
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
    
    game_type = models.CharField(
        max_length=20,
        choices=[
            ("3D", "3D"),
            ("2D", "2D"),
            ("unknown", "Unknown"),
        ],
        default="unknown",
    )

    last_updated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    potential_score = models.PositiveSmallIntegerField(
        default=0,
    )

    evidence_status = models.CharField(
        max_length=30,
        choices=[
            ("demo_available", "Demo Available"),
            ("visual_evidence", "Visual Evidence Available"),
            ("needs_review", "Needs Review"),
        ],
        default="needs_review",
    )
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
    
    
    description = models.TextField(blank=True)

    image_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)



    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Verified Developer"
        verbose_name_plural = "Verified Developers"

    def __str__(self):
        return f"{self.game_name} - {self.developer_name}"
