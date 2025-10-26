from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        next_url = request.POST.get('next') or request.GET.get('next') or 'Home'
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Username or Password'

    return render(request, 'authentication/login.html', {'error':error_message})

@login_required(login_url='login_view')
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('login_view')
        
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {'form':form})


def logout_view(request):
    # Show a confirmation page on GET, perform logout on POST
    if request.method == "POST":
        logout(request)
        return redirect('login_view')

    # For GET requests render a confirmation template so the user can
    # confirm logout (the template already contains a POST form).
    return render(request, 'authentication/logout.html')



