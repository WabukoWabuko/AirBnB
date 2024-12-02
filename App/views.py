from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, User

# Leading to Home/Index page as my landing page.
def Index(request):
    return render(request, "index.html")

# Logging in to an already available account.
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.fullname}!')
            return redirect('dashboard_page')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, "Login.html")

# Creating an account at this point
def SignUp(request):
    # After clicking the button it should submit and go direct to verification page 
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password != confirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(fullname=fullname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
    return render(request, "SignUp.html")

def IDVerification(request):
    # On submitting moves to page 2FA 
    return render(request, "IDVerification.html")

def otherVerification(request):
    return render(request, "otherVerificationWays.html")

def dashboard(request):
    #In Dashboard should display data from the DB
    return render(request, "Dashboard.html")

def bookings(request):
    return render(request, "bookings.html")

def faq(request):
    return render(request, "faq.html")

def feedback(request):
    return render(request, "feedback.html")

def listings(request):
    return render(request, "listings.html")

def messagesM(request):
    return render(request, "messagesM.html")

def payments(request):
    return render(request, "payments.html")

def support(request):
    return render(request, "support.html")

def makeBooking(request):
    return render(request, "makeBooking.html")