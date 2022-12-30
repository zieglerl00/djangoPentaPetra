from django.contrib import admin
from django.urls import path, include
from pentapetra.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]