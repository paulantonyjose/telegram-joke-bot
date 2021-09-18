from django.shortcuts import render
from .models import UserClickCount
from django.views.generic.list import ListView

# Create your views here.
class UserClickCountListView(ListView):
        model = UserClickCount
