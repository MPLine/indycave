from publishers.models import Publisher


class Scout:

    MAX_RESULTS = 5
    MIN_SCORE = 50

    def find_publishers(self, requirements):

        publishers = Publisher.objects.all()

        if requirements.get("game_type"):
            publishers = self._filter_game_type(
                publishers,
                requirements["game_type"]
            )

        results = []

        for publisher in publishers:

            score = self.calculate_score(
                publisher,
                requirements
            )

            if score >= self.MIN_SCORE:
                results.append({
                    "publisher": publisher,
                    "score": score
                })

        # Highest score first.
        # For equal scores, prefer publishers with
        # both a pitch URL and a pitch email.
        results.sort(
            key=lambda result: (
                result["score"],
                bool(result["publisher"].pitch_url),
                bool(result["publisher"].pitch_email),
            ),
            reverse=True
        )

        return results[:self.MAX_RESULTS]


    def calculate_score(self, publisher, requirements):

        score = 0

        game_type = requirements.get("game_type")
        platforms = requirements.get("platforms", [])

        # GAME TYPE — 30 POINTS
        if game_type and game_type.lower() in (
            publisher.game_types_focus or ""
        ).lower():
            score += 30

        # PLATFORMS — 40 POINTS
        if platforms:

            publisher_platforms = [
                platform.strip().lower()
                for platform in (
                    publisher.platforms or ""
                ).split(",")
                if platform.strip()
            ]

            requested_platforms = [
                platform.strip().lower()
                for platform in platforms
                if platform.strip()
            ]

            if requested_platforms:

                points_per_platform = (
                    40 / len(requested_platforms)
                )

                matched_platforms = sum(
                    1
                    for platform in requested_platforms
                    if platform in publisher_platforms
                )

                score += (
                    matched_platforms
                    * points_per_platform
                )

        # PITCH URL — 20 POINTS
        if publisher.pitch_url:
            score += 20

        # PITCH EMAIL — 10 POINTS
        if publisher.pitch_email:
            score += 10

        return score


    def _filter_game_type(self, publishers, game_type):

        game_type = game_type.lower()

        return [
            publisher
            for publisher in publishers
            if game_type in (
                publisher.game_types_focus or ""
            ).lower()
        ]