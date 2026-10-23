
from django import forms
from .models import DeveloperProfile


class DeveloperProfileForm(forms.ModelForm):
    class Meta:
        model = DeveloperProfile
        fields = [
            "email",
            "phone",
            "studio_name",
            "profile_image",
            "facebook_url",
            "x_url",
            "instagram_url",
            "reddit_url",
            "github_url",
        ]

        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your phone number",
            }),
            "studio_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your studio name",
            }),
            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/jpeg,image/png,image/webp",
            }),
            "facebook_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Facebook profile URL",
            }),
            "x_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "X profile URL",
            }),
            "instagram_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Instagram profile URL",
            }),
            "reddit_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Reddit profile URL",
            }),
            "github_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "GitHub profile URL",
            }),
        }

    def clean_profile_image(self):
        image = self.cleaned_data.get("profile_image")

        if image and image.size > 2 * 1024 * 1024:
            raise forms.ValidationError(
                "Profile image must not exceed 2 MB."
            )

        if image:
            allowed_types = [
                "image/jpeg",
                "image/png",
                "image/webp",
            ]

            content_type = getattr(image, "content_type", None)

            if content_type not in allowed_types:
                raise forms.ValidationError(
                    "Please upload a JPG, PNG, or WebP image."
                )

        return image
