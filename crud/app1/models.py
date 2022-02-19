from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title