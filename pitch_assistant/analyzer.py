import re


class IdeaAnalyzer:

    def analyze(self, data):

        game_idea = data.get("game_idea", "").strip()
        gameplay = data.get("gameplay", "").strip()
        special_feature = data.get(
            "special_feature",
            ""
        ).strip()

        combined_text = " ".join([
            game_idea,
            gameplay,
            special_feature
        ]).strip()

        return {
            "core_idea": self._build_core_idea(
                game_idea,
                gameplay
            ),

            "main_hook": self._build_hook(
                special_feature,
                gameplay
            ),

            "unique_selling_point": self._build_usp(
                special_feature
            ),

            "publisher_description": self._build_description(
                game_idea,
                gameplay,
                special_feature
            ),

            "keywords": self._extract_keywords(
                combined_text
            )
        }


    def _build_core_idea(
        self,
        game_idea,
        gameplay
    ):

        if game_idea and gameplay:

            return (
                f"{game_idea} "
                f"The core player experience revolves around "
                f"{self._clean_sentence(gameplay)}"
            )

        if game_idea:

            return game_idea

        return "Your core game idea needs more detail."


    def _build_hook(
        self,
        special_feature,
        gameplay
    ):

        if special_feature:

            return self._make_hook(
                special_feature
            )

        if gameplay:

            return self._make_hook(
                gameplay
            )

        return (
            "The game's main hook needs to be defined more clearly."
        )


    def _build_usp(self, special_feature):

        if special_feature:

            return special_feature

        return (
            "The game's unique selling point needs more detail."
        )


    def _build_description(
        self,
        game_idea,
        gameplay,
        special_feature
    ):

        parts = []

        if game_idea:
            parts.append(
                self._clean_sentence(game_idea)
            )

        if gameplay:
            parts.append(
                "Players "
                + self._lower_first(
                    self._clean_sentence(gameplay)
                )
            )

        if special_feature:
            parts.append(
                "What sets the game apart is "
                + self._lower_first(
                    self._clean_sentence(special_feature)
                )
            )

        return " ".join(parts)


    def _make_hook(self, text):

        text = self._clean_sentence(text)

        if not text:
            return (
                "The game needs a clearer central hook."
            )

        return text


    def _clean_sentence(self, text):

        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        if not text:
            return ""

        return text


    def _lower_first(self, text):

        if not text:
            return text

        return text[0].lower() + text[1:]


    def _extract_keywords(self, text):

        words = re.findall(
            r"\b[a-zA-Z]{4,}\b",
            text.lower()
        )

        stop_words = {
            "this",
            "that",
            "with",
            "from",
            "game",
            "player",
            "players",
            "your",
            "they",
            "their",
            "about",
            "into",
            "where",
            "what",
            "will",
            "have",
            "does",
            "make",
            "makes",
        }

        keywords = []

        for word in words:

            if word not in stop_words and word not in keywords:
                keywords.append(word)

        return keywords[:10]