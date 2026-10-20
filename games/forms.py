
from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    platforms = forms.MultipleChoiceField(
        choices=Game.PLATFORM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Game
        fields = [
            "title",
            "short_description",
            "genre",
            "platforms",
            "development_stage",
            "official_page_url",
            "gameplay_demo_url",
            "cover_image",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your game title",
            }),
            "short_description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Describe your game briefly",
                "rows": 4,
            }),
            "genre": forms.Select(attrs={
                "class": "form-select",
            }),
            "development_stage": forms.Select(attrs={
                "class": "form-select",
            }),
            "official_page_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://...",
            }),
            "gameplay_demo_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://...",
            }),
            "cover_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }
