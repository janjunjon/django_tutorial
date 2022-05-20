from django.db import models

# Create your models here.

class Lead(models.Model):
    id = models.CharField(max_length=50,primary_key=True)