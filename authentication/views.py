from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.contrib.auth import login
from .forms import DeveloperSignUpForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages


def admin_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("indie_dev_scout:dashboard")
        else:
            return redirect("authentication:developer_dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_active:
            login(request, user)
            if user.is_staff:
                return redirect("indie_dev_scout:dashboard")
            else:
                return redirect("authentication:developer_dashboard")

        messages.error(request, "Username oswa password pa kòrèk.")

    return render(request, "authentication/login.html")


def admin_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("authentication:login")

    return redirect("indie_dev_scout:dashboard")



@transaction.atomic
def developer_signup(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("indie_dev_scout:dashboard")
        return redirect("authentication:developer_dashboard")

    if request.method == "POST":
        form = DeveloperSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend",
            )

            return redirect("authentication:developer_dashboard")
    else:
        form = DeveloperSignUpForm()

    return render(
        request,
        "authentication/signup.html",
        {"form": form},
    )





@login_required(login_url="authentication:login")
def developer_dashboard(request):
    if request.user.is_staff:
        return redirect("indie_dev_scout:dashboard")

    profile = getattr(request.user, "developer_profile", None)

    return render(
        request,
        "authentication/developer_dashboard.html",
        {
            "profile": profile,
        },
    )
