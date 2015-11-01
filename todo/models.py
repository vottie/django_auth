from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todo')
    memo = models.CharField('Memo', max_length=128)

