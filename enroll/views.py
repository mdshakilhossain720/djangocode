from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def Add_show(request):
    if request.method =='POST':
        fm=StudentRegistration()
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.changed_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            
    else:
        fm=StudentRegistration()
    return render(request,'enroll/addshow.html',{'form':fm})
