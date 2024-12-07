from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeid = models.CharField(max_length=100)
    employeename = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Schedule(models.Model):
    your_id = models.CharField(max_length=100)
    your_name = models.CharField(max_length=50)
    your_email = models.CharField(max_length=50)
    your_address = models.CharField(max_length=50)
    your_phone = models.CharField(max_length=50)
    your_schedule = models.CharField(max_length=50)
    date = models.CharField(max_length=40)
    message = models.CharField(max_length=100)






