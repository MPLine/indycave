from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        #return redirect("indie_dev_scout:dashboard")
        print("enter")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff and user.is_active:
            login(request, user)
            return redirect("indie_dev_scout:dashboard")

        messages.error(request, "Username oswa password pa kòrèk.")

    return render(request, "authentication/login.html")


def admin_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("authentication:login")

    #return redirect("indie_dev_scout:dashboard")