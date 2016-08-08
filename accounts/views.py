from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm


def signup(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'accounts/regist.html', context)


def root(request):
    return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


def regist_save(request):
    form = RegisterForm(request.POST)
    username = request.POST["username"]
    password = request.POST["password"]
    if form.is_valid():
        form.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'accounts/regist.html', context)

