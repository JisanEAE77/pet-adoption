from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout

def index(request, *args, **kwargs):
    return render(request, "index.html")

def register_view(request):
    errors = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            errors = form.errors.as_data()
            print(request.POST)  # Add this line to print form data
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'errors': errors})

def login_view(request):
    errors = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors.as_data()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'errors': errors})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
def singlepet(request, *args, **kwargs):
    return render(request, "singlepet.html")
