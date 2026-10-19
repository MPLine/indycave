
from datetime import timedelta

from django.utils import timezone


# Maximum score: 100 points
WEIGHTS = {
    "3d_game": 25,
    "demo_available": 25,
    "game_page": 20,
    "recent_activity": 15,
    "commercial_potential": 15,
}


def calculate_potential_score(game):
    """
    Calculate a game's potential score out of 100.

    Accepts a dictionary or an object with the same fields.
    Missing or unverified evidence receives no points.
    """

    def get_value(field, default=None):
        if isinstance(game, dict):
            return game.get(field, default)
        return getattr(game, field, default)

    score = 0

    # 1. 3D game evidence: 25 points
    game_type = get_value("game_type", "unknown")

    if game_type == "3D":
        score += WEIGHTS["3d_game"]

    # 2. Playable demo: 25 points
    demo_url = get_value("demo_url", "")

    if demo_url:
        score += WEIGHTS["demo_available"]

    # 3. Game page with description and visual evidence: 20 points
    description = get_value("description", "")
    image_url = get_value("image_url", "")
    trailer_url = get_value("trailer_url", "")
    website = get_value("website", "")

    has_description = bool(description and description.strip())
    has_visual_evidence = bool(image_url or trailer_url)
    has_game_page = bool(website)

    if has_description and has_visual_evidence and has_game_page:
        score += WEIGHTS["game_page"]

    # 4. Recent development activity: 15 points
    last_updated_at = get_value("last_updated_at")

    if last_updated_at:
        now = timezone.now()

        # Support both timezone-aware and naive datetimes.
        if timezone.is_naive(last_updated_at):
            last_updated_at = timezone.make_aware(last_updated_at)

        if now - last_updated_at <= timedelta(days=180):
            score += WEIGHTS["recent_activity"]

    # 5. Commercial potential: preliminary heuristic, 15 points
    #
    # This is only a rough screening signal, not proof of market demand.
    commercial_signals = 0

    if has_description and len(description.strip()) >= 100:
        commercial_signals += 1

    if has_visual_evidence:
        commercial_signals += 1

    if demo_url:
        commercial_signals += 1

    score += round(
        WEIGHTS["commercial_potential"]
        * commercial_signals / 3
    )
    print(score)
    return min(score, 100)
