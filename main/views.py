from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def add(request):
    return render(request, 'main/add.html')

@login_required
def want(request):
    return render(request, 'main/want.html')

@login_required
def gone(request):
    return render(request, 'main/gone.html')
