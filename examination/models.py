from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    task_type = models.IntegerField(default=0)
    answer = models.CharField(max_length=100)
    clas = models.IntegerField()


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


class AccessCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    used = models.BooleanField(default=False)
    class_level = models.IntegerField()
