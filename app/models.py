from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name