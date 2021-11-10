from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from main.models import Task


class TaskView(ListView):
    """
     this class lists all tasks
    """
    model = Task
    template_name = 'home.html'