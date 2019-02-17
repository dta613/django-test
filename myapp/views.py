# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.views import generic
from django.views.generic import View
from django.views.generic.list import ListView
import json
from django import forms
from django.views.generic.edit import FormView
# Create your views here.


### Current issue loading the views with the templates

def index(request):
    return render(request, 'static/templates/index.html',)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        render("login_success.html", request )
    else:
        #Return an 'invalid' login error message
        render(request, "login_failure.html")

def signup(request, View):
    #print "signing up"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #print form
        if form.is_valid():
            #print "form is valid"
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/form')
    else:
        form = UserCreationForm()
        return render(request, "signup.html", {'form': form})


def logout(request, View):
    return render(request, "logout.html",)
