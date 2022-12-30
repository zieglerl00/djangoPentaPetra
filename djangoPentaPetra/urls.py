from django.contrib import admin
from django.urls import path, include

app_name = "djangoPentaPetra"

urlpatterns = [
    path("auth/", include("authentication.urls")),
    path("", include("pentapetra.urls")),
    path('admin/', admin.site.urls),
]
