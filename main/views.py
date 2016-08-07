import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Restaurant

@login_required
def index(request):
    user = request.user
    context = {
        'restaurants': Restaurant.objects.filter(user_id=user).order_by('id').reverse(),
    }
    return render(request, 'main/index.html', context)

@login_required
def add(request):
    user_id = request.user.id
    restaurant = Restaurant()
    restaurant.user_id = user_id
    restaurant.name = request.POST['name']

    restaurant_type = request.POST['type']
    if restaurant_type: restaurant.restaurant_type = restaurant_type

    scene1 = request.POST['scene1']
    if scene1: restaurant.scene1 = scene1

    scene2 = request.POST['scene2']
    if scene2: restaurant.scene2 = scene2

    station = request.POST['station']
    if station: restaurant.station = station

    score = request.POST['score']
    if score: restaurant.score = score

    url = request.POST['url']
    if url: restaurant.url = url

    memo = request.POST['memo']
    if memo: restaurant.memo = memo

    visited_times = request.POST['visited-times']
    if visited_times: restaurant.visited_times = visited_times

    last_visit_date = request.POST['last-visited-date']
    if last_visit_date:
        restaurant.last_visit_date = datetime.datetime.strptime(last_visit_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    
    restaurant.save()
    return redirect('index')

@login_required
def want(request):
    user = request.user
    context = {
        'restaurants': Restaurant.objects.filter(user_id=user).order_by('id').reverse(),
    }
    return render(request, 'main/want.html', context)

@login_required
def visited(request):
    user = request.user
    context = {
        'restaurants': Restaurant.objects.filter(user_id=user).order_by('id').reverse(),
    }
    return render(request, 'main/visited.html', context)

@login_required
def detail(request):
    return render(request, 'main/detail.html')
