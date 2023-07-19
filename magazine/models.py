from django.db import models
from django.core.management.base import BaseCommand


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Model1(models.Model):
    name = models.CharField(max_length=100)
    # Дополнительные поля модели

    def __str__(self):
        return self.name


class Model2(models.Model):
    name = models.CharField(max_length=100)
    # Дополнительные поля модели

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
