from django.urls import path

from . import views


app_name = "chatbot"


urlpatterns = [
    path("", views.chat, name="chat"),
    path("results/", views.results, name="results"),
    path("new-search/", views.new_search, name="new_search"),
]