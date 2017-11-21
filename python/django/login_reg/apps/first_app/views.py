# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def register(request):
    if request.method != "POST":
        messages.add_message(request, messages.ERROR, "Sorry, gotta add something!")
        return redirect("/")

    person = {
    "first_name" : request.POST["first_name"],
    "last_name" : request.POST["last_name"],
    "birthday" : request.POST["birthday"],
    "email" : request.POST["email"],
    "pw" : request.POST["pw"],
    "confpw" : request.POST["confpw"],
    }

    response = User.objects.addUser(person)

    if response['status'] == False:
        for error in response['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/")
    else:
        messages.add_message(request, messages.SUCCESS, "You have registered!" )
        request.session["first_name"]=person["first_name"]
        return redirect("/success")


def login(request):
    if request.method != "POST":
        messages.add_message(request, messages.ERROR, "Sorry, gotta add something!")
        return redirect("/")

    person = {
        "email" : request.POST["email"],
        "pw" : request.POST["pw"],
    }

    response = User.objects.ValUser(person)

    if response["status"]:
        request.session["first_name"]=response["user"].first_name
        messages.add_message(request, messages.SUCCESS, "You have logged in!" )
        return redirect("/success")
    else:
        messages.add_message(request, messages.ERROR, "YOU'RE NOT REAL")
        return redirect("/")

def success(request):
    return render(request, "first_app/success.html")
