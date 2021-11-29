"""
Module with models for main application
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TimeStampMixin(models.Model):
    """
    Abstract class with date fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyTest(TimeStampMixin):
    """
    Class model tests
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"pk": self.pk})



    def __str__(self):
        return self.name


class Comments(TimeStampMixin):
    """
    Class model comments
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(MyTest, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.author


class Card(TimeStampMixin):
    """
    Class model card
    """
    test = models.ForeignKey(MyTest, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    wrong_answer1 = models.CharField(max_length=200)
    wrong_answer2 = models.CharField(max_length=200)
    wrong_answer3 = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Result(models.Model):
    """
    Class model result after finished test
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(MyTest, on_delete=models.CASCADE)
    flag = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.test} {self.user}"
