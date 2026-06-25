from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    joined_date = models.DateField()

    def __str__(self):
        return self.name
