from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    archived = models.BooleanField(default=False)
