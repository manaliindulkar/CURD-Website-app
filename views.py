from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from employee.forms import NewUserForm

# Create your views here.



def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


def handleSignUp(request):
    if request.method=='POST':

       form=UserCreationForm(request.POST)
       if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, 'Account Created Successfully !!')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loginUser(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'login successfulyy')
                return HttpResponseRedirect('show')
    else:
       form=AuthenticationForm()

    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

