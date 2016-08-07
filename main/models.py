from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    user = models.ForeignKey(User)
    restaurant_type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    scene1 = models.CharField(max_length=20, null=True)
    scene2 = models.CharField(max_length=20, null=True)
    station = models.CharField(max_length=20, null=True)
    score = models.IntegerField(null=True)
    memo = models.TextField(null=True)
    visited_times = models.IntegerField(null=True)
    last_visit_date = models.DateField(auto_now=False, null=True)
    registration_date = models.DateField(auto_now_add=True)
    url = models.URLField(null=True)
    is_active = models.BooleanField(default=True)
