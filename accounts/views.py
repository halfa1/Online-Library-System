from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def index(request):
     """
     Temporary home page to test the Accounts app.
     This will later be replaced with the Bookstore app's index page.
     """
     return render(request, 'accounts/index.html')


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    """
    Handles user login.
    Displays a login form and redirects to the homepage upon successful login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('bookslist')  # Redirect to the temporary home page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to the login page
