"""
Module with views for main application
======================================
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.edit import FormMixin

from main.forms import (CreateFormTest, CreateFormCard,
                        RunTestForm,CommentForm)

from main.models import MyTest, Result
from main.validators import valid_test

#TODO: НУЖНЫ ЛИ РЕЗУЛЬТАТЫ ДЛЯ СОХРАНЕНИЯ?

class TaskView(ListView):
    """
     this class lists all tasks
    """
    model = MyTest
    template_name = 'home.html'


class FilterTest(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user, flag=True)


class SortedBydate(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return MyTest.objects.order_by("-created_at")


class Search(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return MyTest.objects.filter(name__icontains=self.request.GET.get("q"))


class ResultView(ListView):
    model = Result
    template_name = 'info_after_test.html'


class TaskDetailView(FormMixin, DetailView):
    """
    This class shows the detailed information of the task
    """

    model = MyTest
    template_name = 'detail.html'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:detail', kwargs={"pk": self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.test = self.get_object()
        self.object.save()
        return super().form_valid(form)


class TaskRunView(FormView):
    """
    This class run test
    """

    form_class = RunTestForm
    template_name = 'runtest.html'
    success_url = reverse_lazy('main:result')

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        my_test = MyTest.objects.get(id=self.kwargs["pk"])

        initial['questions'] = my_test.card_set.all()
        initial['request'] = self.request
        initial['test'] = my_test

        return initial


class TaskCreateTestView(CreateView):
    """
    This class created new task
    """
    form_class = CreateFormTest
    template_name = 'form_test.html'
    success_url = reverse_lazy('main:form_card')

    def form_valid(self, form):
        """
        Chek valid form, and take request user
        """
        form.instance.user = self.request.user

        return super().form_valid(form)


class CardCreateTestView(CreateView):
    """
    This class created new task
    """

    form_class = CreateFormCard

    template_name = 'form_card.html'
    success_url = reverse_lazy('main:home')

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['tests_queryset'] = MyTest.objects.filter(
            user_id=self.request.user.id)
        return initial

    def form_valid(self, form):
        """
        Chek valid form, and take request user
        """

        valid_test(form.clean().get('test'))
        form.instance.user = self.request.user

        return super().form_valid(form)
