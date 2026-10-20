from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.welcome,name="welcome"),
    path("admin/", admin.site.urls),
    path("chat/", include("chatbot.urls")),
    path("pitch/",include("pitch_assistant.urls")),
    path("APP/", include("authentication.urls")),
    path("indie_dev_scout/",include("indie_dev_scout.urls")),
    path("games/", include("games.urls")),

]