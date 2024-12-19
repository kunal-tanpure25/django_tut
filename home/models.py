from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    feedback = models.TextField(max_length=1000)
