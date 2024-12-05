from django.shortcuts import render, redirect
from django.contrib.auth.models import User as bamdam
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
                messages.success(request, f"Welcome back! {user.username}")
                return redirect('dashboard_page')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

def Logout(request):
    logout(request)

    messages.success(request, "You have successfully logged out.")

    return redirect('login_page')  # Change this to the appropriate page

# Creating an account at this point
def SignUp(request):
    # After clicking the button it should submit and go direct to verification page 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            if bamdam.objects.filter(email=form.cleaned_data.get('email')).exists():
                    messages.error(request, "An account with this email already exists.")
                    return redirect('signup_page')  # Prevent duplicate email

            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                user = bamdam.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=password,
                )
                
                user.set_password(password)
                try:
                    user.save()
                except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
                    return redirect('signup_page')
                form.save()
                messages.success(request, "Account created successfully!")
                return redirect('id_verification_page')
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
            phone = form.cleaned_data.get("phone_number")
            id_document = form.cleaned_data.get("id_card")
            photo = form.cleaned_data.get("current_photo")

            # Add your verification logic here
            
            # Saving the verification details related to the logged-in user
            verification_record = form.save(commit=False) # When True, commit to the DB else not
            verification_record.save()

             # Get the logged-in user's email
            user_email = request.user.email
            #verification_record.email = user_email  # Associate with the logged-in user's email
            

            messages.success(request, "Verification submitted successfully!")
            return redirect("login_page")  # Adjust as needed
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
    

@login_required
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