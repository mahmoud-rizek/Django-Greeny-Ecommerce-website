from django.urls import path
from .views import dashboard, welcome

app_name = 'account'

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("welcome", welcome, name="welcome"),
]
