from django.shortcuts import render, redirect
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
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Query the database for the user with the provided email
            user = User.objects.get(email=email)
            
            # Check if the provided password matches the hashed password in the DB
            if password == user.password:
                # Log the user in
                messages.success(request, f'Welcome back, {user.fullName}!')
                return redirect('dashboard_page')
            else:
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            messages.error(request, 'Email does not exist')

    return render(request, 'Login.html')

# Creating an account at this point
def SignUp(request):
    # After clicking the button it should submit and go direct to verification page 
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password != confirmPassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup_page')

        # if User.objects.filter(fullName=fullName).exists():
        #     messages.error(request, 'Account already exists with this Name.')
        #     return redirect('signup_page')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup_page')

        # Create the user
        User.objects.create(fullName=fullName, email=email, password=password)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('id_verification_page')
    return render(request, "SignUp.html")

# @permission_required
def IDVerification(request):
    email = request.session.get('email') # This helps in retrieving data from the previous session
    user = User.objects.get(email=email)
    
    if email:
        messages.success(request, f"Continue with registration {user.fullName}")
        return redirect('other_verification_ways_page')
        
    userEmail = User.objects.get('email') # I am fetching Email from a different table to use it as an Fk in another table.
    # On submitting moves to page 2FA 
    if request.method == "POST":
        phoneNumber = request.POST.get('phoneNumber')
        idCard = request.FILES.get('idCard')
        currentPhoto = request.FILES.get('currentPhoto')
        
        # Here is saving verification data linked to the user
        UserVerification.objects.create(
            userEmail=userEmail,
            phoneNumber=phoneNumber,
            idCard=idCard,
            currentPhoto=currentPhoto
        )
        messages.success(request, "Verification successful! Fill the code sent to your email/Phone")
        return redirect("other_verification_ways_page")
    return render(request, "IDVerification.html", {'userEmail':userEmail})

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