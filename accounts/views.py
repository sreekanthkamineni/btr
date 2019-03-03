from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


# Create your views here.
def login(request):
    if request.method == 'post':
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return render('index')
 

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
