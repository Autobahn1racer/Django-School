
from django.shortcuts import render,redirect

# Create your views here.
from .models import emp


def login(request):
    if request.method=='POST':
        data=request.POST
        ids=data['loginid']
        pswd=data['password']
        if ids=='Mohan' and pswd=='1234':
            return redirect('register')
        else:
            return render(request,'pass_error.html')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        data=request.POST
        ename=data['name1']
        empid=data['empid']
        newemp=emp(name=ename,empid=empid)
        newemp.save()
        return redirect('details')
    else:
        return render(request,'register.html')
def details(request):
    employees=emp.objects.all()
    return render(request,'details.html',{'employees':employees})
