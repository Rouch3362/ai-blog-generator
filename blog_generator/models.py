from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    body  = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)