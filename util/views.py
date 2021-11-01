from django.contrib.auth.decorators import *
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.http import *

from .forms import RegisterUserForm, UpdateUserInfo

import loginSystem.settings


# Template Paths
REGISTER = 'registration/register.html'
ACCOUNT = 'account/account.html'


@require_safe
def home(request):
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(loginSystem.settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, REGISTER, {'form': form})
    elif request.method == "GET":
        form = RegisterUserForm()
        return render(request, REGISTER, {'form': form})


@login_required
def account(request):
    if request.method == "POST":
        form = UpdateUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, ACCOUNT, {'form': form, 'success': True})
        else:
            return render(request, ACCOUNT, {'form': form})
    elif request.method == "GET":
        form = UpdateUserInfo(instance=request.user)
        return render(request, ACCOUNT, {'form': form})

