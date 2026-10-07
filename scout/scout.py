from publishers.models import Publisher


class Scout:

    MAX_RESULTS = 15
    MIN_SCORE = 50

    def find_publishers(self, requirements):

        publishers = Publisher.objects.all()

        # Filter by game type
        if requirements.get("game_type"):
            publishers = self._filter_game_type(
                publishers,
                requirements["game_type"]
            )

        # Filter by platform
        if requirements.get("platform"):
            publishers = self._filter_platform(
                publishers,
                requirements["platform"]
            )

        # Calculate score
        results = []

        for publisher in publishers:

            score = self.calculate_score(
                publisher,
                requirements
            )

            # Ignore weak matches
            if score >= self.MIN_SCORE:
                results.append({
                    "publisher": publisher,
                    "score": score
                })

        # Best matches first
        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        # Maximum 15 publishers
        return results[:self.MAX_RESULTS]

    def calculate_score(self, publisher, requirements):

        score = 0

        game_type = requirements.get("game_type")
        platform = requirements.get("platform")

        # Game type match = 50 points
        if game_type:
            if game_type.lower() in publisher.game_types_focus.lower():
                score += 50

        # Platform match = 50 points
        if platform:
            if platform.lower() in publisher.platforms.lower():
                score += 50

        return score

    def _filter_game_type(self, publishers, game_type):

        game_type = game_type.lower()

        return [
            publisher
            for publisher in publishers
            if game_type in publisher.game_types_focus.lower()
        ]

    def _filter_platform(self, publishers, platform):

        platform = platform.lower()

        return [
            publisher
            for publisher in publishers
            if platform in publisher.platforms.lower()
        ]