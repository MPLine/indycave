
from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path("add/", views.add_game, name="add_game"),
    path("<int:game_id>/", views.game_detail, name="game_detail"),
    path("<int:game_id>/", views.game_detail, name="game_detail"),
]
