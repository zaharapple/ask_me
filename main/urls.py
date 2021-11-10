"""
Urls main application
=====================
"""
from django.urls import path

from main.views import TaskView


app_name = "main"
urlpatterns = [
    path('', TaskView.as_view(), name="home"),

]