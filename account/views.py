from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from account.forms import editprofileform
from  django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# from django.response import HttpResponse
# Create your views here

def editprofile(request):
    if request.method=="POST":
        form=editprofileform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form=editprofileform(instance=request.user)
        args={'form':form}
        return render(request,'account/editprofile.html',args)

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/profile')
    else:
        form=PasswordChangeForm(request.user)
        args={'form':form}
        return render(request,"account/change_password.html" ,args)



def home(request):
    return render(request, "account/home.html")

def profile(request):
    args={'user':request.user}
    print(request.user)
    return render(request,"account/profile.html" ,args)

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=UserCreationForm()
        args={'form':form}

        return render(request,"account/register.html",args)