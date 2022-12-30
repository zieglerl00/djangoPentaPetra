from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, req, *args, **kwargs):
        return render(req, "pentapetra/home.html")
