from django.db import models
from django.utils import timezone
# Create your models here.

class Patient(models.Model):
    Name =models.TextField()
    DOB =models.DateField()

