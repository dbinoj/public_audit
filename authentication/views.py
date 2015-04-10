from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import logout
from authentication.forms import login_userForm
 
def index(request):
    if request.user.is_authenticated():
        return redirect('client:index')
    else:
        return redirect('authentication:login_user')

def login_user(request):
    return render_to_response('authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('authentication:index')