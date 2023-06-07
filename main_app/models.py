from django.db import models


# import user
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    url = models.CharField(max_length=500)
    urlImage = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
