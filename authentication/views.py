from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginUserForm


 
def index(request):
    if request.user.is_authenticated():
        return redirect('client:index')

    else:
        return redirect('authentication:login_user')

def login_user(request):
    form = LoginUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'client/index.html')
        else:
            return render(request, 'authentication/login.html', {"form": form})
               
    else:
        return render(request, 'authentication/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('authentication:index')