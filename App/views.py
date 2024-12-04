from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import * # Which are Booking, User, UserVerification, Listing, Amenity, PropertyPhoto,
                    #Payment, Review, Message, Notification, SupportTicket, BlackList, SecurityAlert,
                    #GeoTracking, Discount

# Leading to Home/Index page as my landing page.
def Index(request):
    return render(request, "index.html")

# Logging in to an already available account.
def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Welcome back!")
                return redirect('dashboard_page')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})


# Creating an account at this point
def SignUp(request):
    # After clicking the button it should submit and go direct to verification page 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                User.objects.create_user(
                    fullName=form.cleaned_data.get('fullName'),
                    email=form.cleaned_data.get('email'),
                    password=password,
                )
                messages.success(request, "Account created successfully!")
                return redirect('login_page')
            else:
                messages.error(request, "Passwords do not match.")
    else:
        form = SignupForm()
    return render(request, 'SignUp.html', {'form': form})

def IDVerification(request):
    if request.method == "POST":
        form = IdentityVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data (e.g., save files, validate, etc.)
            phone_number = form.cleaned_data.get("phone_number")
            id_card = form.cleaned_data.get("id_card")
            current_photo = form.cleaned_data.get("current_photo")

            # Add your verification logic here

            messages.success(request, "Verification submitted successfully!")
            return redirect("verification_success")  # Adjust as needed
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = IdentityVerificationForm()
    return render(request, "IDVerification.html", {"form": form})


def otherVerification(request):
    if request.method == "POST":
        form = AuthenticationCodeForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data.get("verification_code")
            
            # Add logic to verify the code here
            
            messages.success(request, "Authentication successful!")
            return redirect("success_page")  # Replace with the actual success URL
        else:
            messages.error(request, "Invalid verification code.")
    else:
        form = AuthenticationCodeForm()
    return render(request, "otherVerificationWays.html", {"form": form})
    


def dashboard(request):
    #In Dashboard should display data from the DB
    data = User.objects.all()
    return render(request, "Dashboard.html", {'data': data})

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