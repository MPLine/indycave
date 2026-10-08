from django.urls import path

from . import views


app_name = "pitch_assistant"


urlpatterns = [

    path(
        "",
        views.idea,
        name="idea"
    ),

    path(
        "analyze/",
        views.analyze_idea,
        name="analyze"
    ),

    path(
        "new/",
        views.new_pitch,
        name="new_pitch"
    ),

]