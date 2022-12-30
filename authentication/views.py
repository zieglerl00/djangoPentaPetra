from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from authentication.forms import LoginForm


class LoginView(View):
    form_class = LoginForm

    def get(self, req, *args, **kwargs):
        form = self.form_class
        return render(
            req,
            "authentication/login.html",
            {"form": form}
        )

    def post(self, req, *args, **kwargs):
        form = self.form_class(data=req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                return HttpResponse("Succesfull")
            else:
                return HttpResponse("Wrong credentials")

        else:
            return HttpResponse("form not valid!")


class LogoutView(View):
    def get(self, req, *args, **kwargs):
        user = req.user
        if isinstance(user, AnonymousUser):
            return HttpResponse("You havent logged in yet.")
        else:
            logout(req)
            return HttpResponse("Logged out")


class ProtectedView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "redirect_to"

    def get(self, req, *args, **kwargs):
        user = req.user

        if isinstance(user, AnonymousUser):
            return HttpResponse("Not allowed")

        return HttpResponse("Protected")
