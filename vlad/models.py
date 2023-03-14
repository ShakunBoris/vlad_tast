from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    
class Parse(models.Model):
    time = models.DateTimeField(auto_now_add=True)

class Currency(models.Model):
    cur = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    call_id = models.ForeignKey(Parse, null=True, on_delete=models.CASCADE, related_name='currency_by_parse')


