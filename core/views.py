from contextlib import nullcontext

from django.shortcuts import render, redirect
from item.models import Category, Music
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from .forms import SignupForm

# @login_required(login_url="/signup/")
def index(request):
    items = Music.objects.filter()[0:20]
    categories = Category.objects.all()
    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"].lower()
            user.username = form.cleaned_data["username"].lower()
            user.save()
            login(request, user)
            return redirect("/login/")
    else:
        form = SignupForm()

    return render(
        request,
        "core/signup.html",
        {
            "form": form,
        },
    )


def logout_view(request):
    logout(request)
    return redirect(
        "/login/"
    )  # Replace 'home' with the name of the URL pattern for your home page
