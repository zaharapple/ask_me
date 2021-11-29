"""
Urls main application
=====================
"""
from django.urls import path
from main.views import (TaskView, TaskCreateTestView, CardCreateTestView,
                        TaskDetailView, TaskRunView, ResultView,
                        Search, FilterTest, SortedBydate,
                        )

app_name = "main"
urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('search/', Search.as_view(), name="search"),
    path('filter/', FilterTest.as_view(), name="filter"),
    path('sorted/', SortedBydate.as_view(), name="sort"),
    path('form/', TaskCreateTestView.as_view(), name='form_task'),
    path('form/card', CardCreateTestView.as_view(), name='form_card'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('test/<int:pk>/', TaskRunView.as_view(), name='run_test'),
    path('result/', ResultView.as_view(), name="result"),
]
