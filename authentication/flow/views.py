from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import  redirect
from .forms import LoginForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page after successful login
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # This method sends a password reset email to the user associated with the given email address
            form.save(request=request)
            messages.success(request, 'Password reset email has been sent. Check your inbox.')
    else:
        form = PasswordResetForm()
    return render(request, 'reset_password.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'profile.html')

