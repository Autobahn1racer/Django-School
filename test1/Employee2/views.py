from django.shortcuts import render

# Create your views here.
from .models import emp

def login(request):
    if request.method==='POST':
        data=request.POST
        ids=data['loginid']
        pswd=data['password']
        if ids=='Mohan' and pswd=='1234':
            return redirect('register')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
