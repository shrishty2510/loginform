from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib import messages
from . forms import MainUser,Extenduser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import SignUp
from . forms import Signin_form




def sign_up(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST['user_type']
        image = request.FILES['profile_image']
        locality = request.POST['locality']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        if password1 != password2:
            messages.error(request,"password does not matched!")  
        elif User.objects.filter(username = user).first():
            messages.error(request, "This username is already taken")
            return HttpResponseRedirect('/')    
        else:    
            user1 = User.objects.create_user(user, email, password1)
            user1.first_name=fname
            user1.last_name=lname
            user1.save()
            user = User.objects.get(username=user)
            print(user)
            us2 = SignUp(user=user,user_type=user_type, profile_image=image, locality=locality,city=city,state=state,pin=pin)
            print(user)
            us2.save()
            messages.success(request,"signup successfully")
            return HttpResponseRedirect('/')
    return render(request,'core/home.html',{'form1':MainUser,'form2':Extenduser})

        
def loginform(request):
    if request.method == 'POST':
        fr = Signin_form(data=request.POST)
        if fr.is_valid():
            data=fr.cleaned_data
            uname=data['Username']
            upass=data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Sucessfully!!')
                return HttpResponseRedirect('/profile/')
    else:        
        fr = Signin_form()
    return render(request,'core/login.html',{'form':fr})   


def logoutform(request):
    logout(request)
    return HttpResponseRedirect('/login/')   

def profilepage(request):
    if request.user.is_authenticated:
            us = User.objects.get(username = request.user)
            us1 = SignUp.objects.get(user= request.user)
            return render(request,'core/profile.html',{'user':us,'detail':us1})
    else:
        return HttpResponseRedirect('/login/')    