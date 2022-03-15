from django.shortcuts import render
from design.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from .forms import *



# Create your views here.
def navigation(request):
    return render(request,'base.html')

def Signup(request):
    if request.method == 'POST':
       fname = request.POST["firstname"]
       print(fname)
       lname = request.POST["lastname"]
       pwd =  request.POST["password"]
       cpwd = request.POST["confirm_password"]
       uname = request.POST["username"]
       em = request.POST["email"]
       con= request.POST["contact"]
       if (pwd == cpwd):
         data = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email= em,password=pwd)
         d = SignUp()
         d.user = data
         d.contact = con
         d.save()
         return HttpResponse ("Data saved successfully!")
       else:
           return HttpResponse ("password and confirm password are not same!")

    return render(request,'signup.html') 

def Login(request):
    if request.method == 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       u = authenticate(username=username,password=password)
       if u is not None:
          login(request,u)
          return HttpResponseRedirect("joblist")
       else:
          return HttpResponse('Username or password is incorrect')
    return render(request,'login.html')


def JobList(request):
    jobs = Joblist.objects.all()
    context = {'jobs': jobs}
    return render(request,"joblist.html",context)

# def apply(request):
#     if request.method == 'POST':
#         documents = request.FILES["files"]
#         uname = request.POST["username"]
#         em = request.POST["email"]
#         data = Apply(username = uname,email = em,documents=documents)
#         data.save()
#     return render(request,'apply.html')

def apply(request):
    form = applyform()
    if request.method == 'POST':
        form = applyform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'apply.html')
    context = {'form':form}
    return render(request,'apply.html',context)

#just for  jenkins webhooks testing


