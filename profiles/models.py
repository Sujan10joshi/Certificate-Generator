from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=50)
