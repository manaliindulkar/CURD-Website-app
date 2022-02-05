from django.contrib import admin
from .models import Employee,Log,SignUp
# Register your models here.
@admin.register(Employee)
class UserEmployee(admin.ModelAdmin):
    list_display =('eid','eemail','ename','econtact')

@admin.register(Log)
class UserLogin(admin.ModelAdmin):
    a =('username','password')

@admin.register(SignUp)
class UserSign(admin.ModelAdmin):
    b =('username','address','password','email','contact')
