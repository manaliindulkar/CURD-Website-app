from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

class Log(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table = "login"

class SignUp(models.Model):
    username = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField(max_length=15)
    class Meta:
        db_table = "signup"
