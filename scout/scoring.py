def calculate_score(self, publisher, requirements):

    score = 0

    game_type = requirements.get("game_type")
    platforms = requirements.get("platforms", [])

    # -------------------------
    # GAME TYPE = 30 POINTS
    # -------------------------
    if game_type:
        if game_type.lower() in publisher.game_types_focus.lower():
            score += 30

    # -------------------------
    # PLATFORMS = 40 POINTS
    # -------------------------
    
# PLATFORMS — 40 POINTS
    if platforms:

        publisher_platforms = [
            p.strip().lower()
            for p in (publisher.platforms or "").split(",")
        ]

        requested_platforms = [
            p.strip().lower()
            for p in platforms
        ]

        matched_platforms = sum(
            1
            for platform in requested_platforms
            if platform in publisher_platforms
        )

        if requested_platforms:
            points_per_platform = 40 / len(requested_platforms)

            score += matched_platforms * points_per_platform


    # -------------------------
    # PITCH URL = 20 POINTS
    # PITCH EMAIL = 10 POINTS
    # -------------------------
    if publisher.pitch_url:
        score += 20

    elif publisher.pitch_email:
        score += 10

    return score