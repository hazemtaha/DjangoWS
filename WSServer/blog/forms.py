# encoding: utf-8

from django import forms
from django.contrib.auth.models import User
from models import Users
from models import *



class RegistrationForm(forms.Form):
    email = forms.CharField()
    password=forms.CharField()


class LoginForm(forms.Form):
    email = forms.CharField()
    password=forms.CharField()

class Posts (forms.Form):
    title = forms.CharField()
    body = forms.TextField()

