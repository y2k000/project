from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUser,CreateUserProf
from .models import UserDetails
from django.http import HttpResponse
import uuid

def signin_user(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:   
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('Invalid user')
    return render(request, 'signin.html')

def signup_user(request):
    context = {}
    userform = CreateUser()
    userform1 = CreateUserProf() 
    context['form'] = userform
    context['form1'] = userform1
    userid = uuid.uuid4()
    if request.method == 'POST':        
        userdetails = CreateUser(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        mobile = request.POST["mobile"]
        user_profile_picture = request.FILES["user_profile_picture"]

        userdetails1 = UserDetails(userid = userid,username = username,email=email,firstname=first_name,lastname=last_name,mobile=mobile,user_profile_picture=user_profile_picture)      
        if userdetails.is_valid():
            userdetails.save()
            userdetails1.save()            
        else:
            print(userdetails.errors)
            return HttpResponse('Signing up is not complete')
    return render(request, 'signup.html', context)

def logoutuser(request):
    logout(request)
    return render(request, 'signin.html')
@login_required(login_url='signin')

def home(request):
    return render(request, 'home.html')

