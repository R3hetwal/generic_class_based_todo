from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import NewUser
from todo.views import *

def home_view(request):
    return render (request,'home.html')

def error_page(request):
    return render(request, '404.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('tasks')

            else:
                form.add_error(None, 'Invalid email or password')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



















# from django.shortcuts import render, redirect
# from .forms import LoginForm, SignupForm

# # Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # Handle a successful form submission
#             # ...
#             return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # Handle a successful form submission
#             # ...
#             return redirect('home')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})
