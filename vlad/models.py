from django.db import models

# Create your models here.
class Currency(models.Model):
    cur = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
