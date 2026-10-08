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
    if platforms:

        publisher_platforms = [
            p.strip().lower()
            for p in publisher.platforms.split(",")
        ]

        matched_platforms = 0

        for platform in platforms:
            if platform.lower() in publisher_platforms:
                matched_platforms += 1

        platform_score = (
            matched_platforms / len(platforms)
        ) * 40

        score += platform_score

    # -------------------------
    # PITCH URL = 20 POINTS
    # PITCH EMAIL = 10 POINTS
    # -------------------------
    if publisher.pitch_url:
        score += 20

    elif publisher.pitch_email:
        score += 10

    return score