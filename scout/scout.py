from publishers.models import Publisher


class Scout:

    MAX_RESULTS = 15
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

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        return results[:self.MAX_RESULTS]

    def calculate_score(self, publisher, requirements):

        score = 0

        game_type = requirements.get("game_type")
        platforms = requirements.get("platforms", [])

        # -------------------------
        # GAME TYPE — 30 POINTS
        # -------------------------
        if game_type:

            if game_type.lower() in publisher.game_types_focus.lower():
                score += 30

        # -------------------------
        # PLATFORMS — 40 POINTS
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
        # PITCH URL — 20 POINTS
        # -------------------------
        if publisher.pitch_url:
            score += 20

        # -------------------------
        # PITCH EMAIL — 10 POINTS
        # -------------------------
        if publisher.pitch_email:
            score += 10

        return score

    def _filter_game_type(self, publishers, game_type):

        game_type = game_type.lower()

        return [
            publisher
            for publisher in publishers
            if game_type in publisher.game_types_focus.lower()
        ]