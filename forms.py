from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from employee.models import Employee
from employee.models import Log
from employee.models import SignUp
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = "__all__"



class NewUserForm(UserCreationForm):


	class Meta:
		model = User
		fields = ("username",  "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user