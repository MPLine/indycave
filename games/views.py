
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GameForm
from .models import Game, GamePublisherMatch
from scout.scout import Scout


def find_and_save_publishers(game):
    """
    Automatically find publisher matches for a saved game
    and store them for admin review.
    """

    # Convert saved platform codes into readable labels.
    platform_labels = dict(Game.PLATFORM_CHOICES)

    requirements = {
        "game_type": game.genre,
        "platforms": [
            platform_labels.get(platform, platform)
            for platform in game.platforms
        ],
    }

    scout = Scout()
    results = scout.find_publishers(requirements)

    matched_publisher_ids = []

    for result in results:
        publisher = result["publisher"]
        score = round(result["score"])

        matched_publisher_ids.append(publisher.pk)

        match, created = GamePublisherMatch.objects.update_or_create(
            game=game,
            publisher=publisher,
            defaults={
                "match_score": score,
            },
        )

        # Do not reset a match that has already been sent.
        # New matches remain pending for admin review.
        if created:
            match.status = "pending"
            match.save(update_fields=["status", "updated_at"])

    # Remove outdated pending matches if the game is resubmitted.
    GamePublisherMatch.objects.filter(
        game=game,
        status="pending",
    ).exclude(
        publisher_id__in=matched_publisher_ids,
    ).delete()

    return results


@login_required
def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)

        if form.is_valid():
            game = form.save(commit=False)
            game.developer = request.user
            game.save()

            # Automatically run Scout after the game is saved.
            find_and_save_publishers(game)

            return redirect("authentication:developer_dashboard")
    else:
        form = GameForm()

    return render(
        request,
        "games/add_game.html",
        {"form": form},
    )


@login_required
def game_detail(request, game_id):
    game = get_object_or_404(
        Game,
        id=game_id,
        developer=request.user,
    )

    publisher_matches = GamePublisherMatch.objects.filter(
        game=game,
        status="sent",
    ).select_related(
        "publisher"
    ).order_by(
        "-match_score"
    )

    return render(
        request,
        "games/game_detail.html",
        {
            "game": game,
            "publisher_matches": publisher_matches,
        },
    )
