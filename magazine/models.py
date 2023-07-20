from django.db import models
from django.utils import timezone
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
    age = models.IntegerField(default=0)
    email = models.EmailField(default='example@example.com')
    date_created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Model2(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='model2_images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200, default='Default description')

    def __str__(self):
        return self.name
