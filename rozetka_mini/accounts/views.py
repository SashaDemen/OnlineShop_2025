from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User

def signup(request):
    class SignUpForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = User
            fields = ("username","password1","password2")
    if request.method == "POST":
        role = request.POST.get("role","buyer")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = role
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})
