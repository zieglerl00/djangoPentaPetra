from django.forms import forms, CharField, PasswordInput


class LoginForm(forms.Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
