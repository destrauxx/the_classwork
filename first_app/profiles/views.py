from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LoginForm
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    return render(request, 'profiles/forms.html', {'form': form})