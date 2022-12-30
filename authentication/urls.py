from django.contrib import admin
from django.urls import path
from .views import *

app_name = "authentication"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("protected", ProtectedView.as_view(), name="protected"),
]
