from django.urls import path
from .views import dashboard, welcome, sign_up, user_activate

app_name = 'account'

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("welcome", welcome, name="welcome"),
    path("sign-up", sign_up, name="signup"),
    path("<str:username>/activate", user_activate, name="user_activate"),
]
