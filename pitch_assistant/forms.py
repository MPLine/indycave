from django import forms


class IdeaForm(forms.Form):

    game_title = forms.CharField(
        label="Game Title",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your game title",
            }
        )
    )

    game_genre = forms.ChoiceField(
        label="Game Genre",
        choices=[
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Arcade", "Arcade"),
            ("Fighting", "Fighting"),
            ("FPS", "FPS"),
            ("Horror", "Horror"),
            ("Narrative", "Narrative"),
            ("Platformer", "Platformer"),
            ("Puzzle", "Puzzle"),
            ("RPG", "RPG"),
            ("Racing", "Racing"),
            ("Roguelike", "Roguelike"),
            ("Simulation", "Simulation"),
            ("Sports", "Sports"),
            ("Strategy", "Strategy"),
            ("Survival", "Survival"),
            ("Tactical", "Tactical"),
            ("Turn-based", "Turn-based"),
            ("Sandbox", "Sandbox"),
            ("City Builder", "City Builder"),
            ("Deckbuilder", "Deckbuilder"),
            ("4X", "4X"),
            ("RTS", "RTS"),
            ("Stealth", "Stealth"),
            ("Co-op", "Co-op"),
            ("Multiplayer", "Multiplayer"),
            ("Casual", "Casual"),
            ("Other", "Other"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )

    game_idea = forms.CharField(
        label="Tell us about your game",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 7,
                "placeholder": (
                    "Describe your game naturally. "
                    "What does the player do? "
                    "What is the game about? "
                    "How does it work?"
                ),
            }
        )
    )

    special_feature = forms.CharField(
        label="What makes your game special?",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": (
                    "What makes your game different or interesting? "
                    "It could be a mechanic, story, world, art style, "
                    "player experience, or anything else."
                ),
            }
        )
    )