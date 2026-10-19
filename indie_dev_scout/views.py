
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from .models import DiscoveredDeveloper, VerifiedDeveloper
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db import IntegrityError, transaction

from .models import DiscoveredDeveloper, VerifiedDeveloper
from .services.search_service import search_all_sources

@staff_member_required(login_url="/auth/login/")
def dashboard(request):
    context = {
        "total_discovered": DiscoveredDeveloper.objects.count(),
        "pending_review": DiscoveredDeveloper.objects.filter(
            status="pending"
        ).count(),
        "total_verified": VerifiedDeveloper.objects.count(),
        "emails_sent": VerifiedDeveloper.objects.filter(
            email_sent=True
        ).count(),
        "discovered_developers": DiscoveredDeveloper.objects.filter(
            status="pending"
        ).order_by("-discovered_at"),
    }

    return render(
        request,
        "indie_dev_scout/dashboard.html",
        context,
    )

@staff_member_required(login_url="/auth/login/")
@require_POST
def approve_developer(request, developer_id):
    with transaction.atomic():
        developer = get_object_or_404(
            DiscoveredDeveloper.objects.select_for_update(),
            pk=developer_id,
            status="pending",
        )

        # Evite kreye menm kontak la de fwa.
        existing = VerifiedDeveloper.objects.filter(
            source_url=developer.source_url,
            game_name=developer.game_name,
            developer_name=developer.developer_name,
        ).first()

        if not existing:
            VerifiedDeveloper.objects.create(
                developer_name=developer.developer_name,
                game_name=developer.game_name,
                platforms=developer.platforms,
                website=developer.website,
                contact_email=developer.contact_email,
                source_name=developer.source_name,
                source_url=developer.source_url,
                is_verified=True,
            )

        developer.status = "approved"
        developer.reviewed_at = timezone.now()
        developer.save(update_fields=["status", "reviewed_at"])

    messages.success(
        request,
        f"{developer.game_name} has been approved."
    )
    return redirect("indie_dev_scout:dashboard")


@staff_member_required(login_url="/auth/login/")
@require_POST
def reject_developer(request, developer_id):
    developer = get_object_or_404(
        DiscoveredDeveloper,
        pk=developer_id,
        status="pending",
    )

    developer.status = "rejected"
    developer.reviewed_at = timezone.now()
    developer.save(update_fields=["status", "reviewed_at"])

    messages.success(
        request,
        f"{developer.game_name} has been rejected."
    )
    return redirect("indie_dev_scout:dashboard")

@staff_member_required(login_url="/auth/login/")
@require_POST
def search_developers(request):
    try:
        results = search_all_sources(limit=30)
    except Exception:
        messages.error(
            request,
            "Search failed. Please try again."
        )
        return redirect("indie_dev_scout:dashboard")

    added = 0
    duplicates = 0

    for item in results:
        exists = DiscoveredDeveloper.objects.filter(
            source_url=item["source_url"]
        ).exists()

        verified_exists = VerifiedDeveloper.objects.filter(
            source_url=item["source_url"]
        ).exists()

        if exists or verified_exists:
            duplicates += 1
            continue

        try:
            DiscoveredDeveloper.objects.create(
                developer_name=item["developer_name"],
                game_name=item["game_name"],
                platforms=item["platforms"],
                website=item["website"],
                contact_email=item["contact_email"],
                source_name=item["source_name"],
                source_url=item["source_url"],
                potential_score=item["potential_score"],
                
               

            )
            added += 1
        except IntegrityError:
            duplicates += 1

    messages.success(
        request,
        f"Search complete: {added} new results added, "
        f"{duplicates} duplicates skipped."
    )

    return redirect("indie_dev_scout:dashboard")
