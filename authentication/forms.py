
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import DeveloperProfile


class DeveloperSignUpForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Choose a username",
        }),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your email address",
        }),
    )

    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your phone number",
        }),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Create a password",
        }),
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm your password",
        }),
    )

    studio_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Studio name (optional)",
        }),
    )

    facebook_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Facebook profile URL (optional)",
        }),
    )

    x_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "X profile URL (optional)",
        }),
    )

    instagram_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Instagram profile URL (optional)",
        }),
    )

    reddit_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Reddit profile URL (optional)",
        }),
    )

    github_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "GitHub profile URL (optional)",
        }),
    )

    def clean_username(self):
        username = self.cleaned_data["username"].strip()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "This username is already taken."
            )

        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error(
                "confirm_password",
                "Passwords do not match.",
            )

        return cleaned_data

    def save(self):
        data = self.cleaned_data

        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )

        DeveloperProfile.objects.create(
            user=user,
            email=data["email"],
            phone=data["phone"],
            studio_name=data.get("studio_name", ""),
            facebook_url=data.get("facebook_url", ""),
            x_url=data.get("x_url", ""),
            instagram_url=data.get("instagram_url", ""),
            reddit_url=data.get("reddit_url", ""),
            github_url=data.get("github_url", ""),
        )

        return user
