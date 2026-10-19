from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("", views.admin_login, name="login"),
    path("signup/", views.developer_signup, name="signup"),
    path("logout/", views.admin_logout, name="logout"),
    path(   "dashboard/",views.developer_dashboard, name="developer_dashboard",),

]