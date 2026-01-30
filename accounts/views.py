from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        # すでにログイン済みなら home
        return redirect("accounts:home")

    form = LoginForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user:
            login(request, user)
            return redirect("accounts:home")
        error = "ユーザー名かパスワードが違います"

    return render(request, "accounts/login.html", {"form": form, "error": error})

def signup_view(request):
    form = SignupForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        Profile.objects.create(user=user, age=form.cleaned_data["age"])
        login(request, user)
        return redirect("accounts:home")

    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("accounts:login")

@login_required
def home_view(request):
    return HttpResponse("Home (仮) - ログイン成功！")

@login_required
def home_view(request):
    return render(request, "accounts/home.html")

