from django.db import models
from django.urls import reverse


# import user
from django.contrib.auth.models import User
# Create your models here.


class ReadingList(models.Model):
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    url = models.CharField(max_length=500)
    urlImage = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    readingList = models.ManyToManyField(ReadingList)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', kwargs={'article_id': self.id})
