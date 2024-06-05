from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=70)
    dob = models.DateField()
    gender = models.CharField(max_length=25)
    password = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
