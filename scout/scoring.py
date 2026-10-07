def calculate_score(publisher, requirements):

    score = 0

    game_type = requirements.get("game_type")
    platform = requirements.get("platform")

    if game_type:
        if game_type.lower() in publisher.game_types_focus.lower():
            score += 50

    if platform:
        if platform.lower() in publisher.platforms.lower():
            score += 50

    return score