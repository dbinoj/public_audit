from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginUserForm


 
def index(request):
    if request.user.is_authenticated():
        if request.user.groups.filter(name="client").exists():
            return redirect('client:index')

        elif request.user.groups.filter(name="storage").exists():
            return redirect('storage:index')

        elif request.user.groups.filter(name="tpa").exists():
            return redirect('tpa:index')
    return redirect('authentication:login_user')

def login_user(request):
    form = LoginUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name="client").exists():
                login(request, user)
                return redirect('client:index')

            elif user.groups.filter(name="storage").exists():
                login(request, user)
                return redirect('storage:index')

            elif user.groups.filter(name="tpa").exists():
                login(request, user)
                return redirect('tpa:index')
    return render(request, 'authentication/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('authentication:login_user')