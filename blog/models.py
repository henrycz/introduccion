from django.db import models
from django.db.models.base import Model

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):
        return self.title