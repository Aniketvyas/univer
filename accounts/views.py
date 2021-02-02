from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from  module.models import *
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        type=request.POST['type']
        username = request.POST['email']
        passw = request.POST['password']
        user= auth.authenticate(username=username ,password=passw)
        if user is not None:
            auth.login(request,user)
        else:
            messages.error(request,'Error occured, Try Again!!')
            return redirect('accounts/login')
    else:
        messages.error(request,'Bad Request!!')

def logout(request):
    auth.logout(request)
    return redirect('/')