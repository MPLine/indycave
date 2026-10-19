
from django.urls import path
from . import views

app_name = "indie_dev_scout"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        "approve/<int:developer_id>/",
        views.approve_developer,
        name="approve_developer",
    ),
    path(
        "reject/<int:developer_id>/",
        views.reject_developer,
        name="reject_developer",
    ),
    path("search/",views.search_developers,name="search_developers",
    ),
]
