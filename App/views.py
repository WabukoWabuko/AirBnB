from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect, get_object_or_404
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


@csrf_exempt
def report_emergency(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            keyword = data.get('keyword', '')
            location = data.get('location', {})
            timestamp = data.get('timestamp', '')

            # Log or process the data
            print("Emergency Detected:")
            print(f"Keyword: {keyword}")
            print(f"Location: {location}")
            print(f"Timestamp: {timestamp}")

            # Optional: Save to database
            messages.error(request, f"{keyword} - {location} - {timestamp}")
            # Emergency.objects.create(keyword=keyword, latitude=location['latitude'], longitude=location['longitude'], timestamp=timestamp)

            return JsonResponse({'status': 'success', 'message': 'Emergency reported!'})
        except Exception as e:
            print("Error processing emergency data: ", e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


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
    user = request.user
    try:
        verification = UserVerification.objects.get(email=user.id)
        profile_picture = verification.photo.url if verification.photo else None
    except UserVerification.DoesNotExist:
        profile_picture = None
    return render(request, "Dashboard.html", {'data': data,
                                              'user': user,
                                              'profile_picture': profile_picture})

@login_required
def bookings(request):
    if request.user.is_authenticated:
        # Fetch all bookings for the logged-in user
        bookings = Booking.objects.filter(guest=request.user.id)
    else:
        # Handle the case where the user is not authenticated (optional)
        bookings = []

    # Pass bookings data to the template
    context = {
        'bookings': bookings
    }

    return render(request, 'bookings.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Prompt confirmation for cancellation
    if request.method == 'POST':
        booking.delete()  # Delete the booking
        messages.success(request, "Booking has been cancelled successfully.")
        return redirect('bookings_page')
    
    return render(request, 'cancel_confirmation.html', {'booking': booking})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user.id)

    if request.method == 'POST':
        booking.delete()  # Delete the booking

        messages.success(request, "Your booking has been cancelled successfully.")
        return redirect('bookings_page')

    return render(request, 'cancel_confirmation.html', {'booking': booking})

def faq(request):
    return render(request, "faq.html")

def feedback(request):
    return render(request, "feedback.html")

def listings(request):
    return render(request, "listings.html")

def messagesM(request):
    dataMessages = Message.objects.all()
    return render(request, "messagesM.html", {'dataMessages': dataMessages})

def delete_message(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(Message, id=message_id)
        message.delete()
        messages.success(request, "Message deleted successfully.")
        return redirect('messages_page')
    return render(request, "messagesM.html")

def payments(request):
    return render(request, "payments.html")

def support(request):
    return render(request, "support.html")

def makeBooking(request):
    return render(request, "makeBooking.html")
    
from django.contrib.auth import get_user_model
User = get_user_model()
def compose_message(request):
    if request.method == "POST":
        sender = request.user  # Assumes the user is authenticated
        receiver_id = request.POST.get('receiver')
        content = request.POST.get('content')
        
        print(f"Receiver ID: {receiver_id}")  # Debugging step

        try:
            receiver = User.objects.get(id=receiver_id)
            Message.objects.create(sender=sender, receiver=receiver, content=content)
            messages.success(request, "Message sent successfully!")
        except User.DoesNotExist:
            messages.error(request, "Recipient does not exist.")
        return redirect('messages_page')


@login_required
def profile(request):
    user = request.user  # Get the logged-in user
    verification = UserVerification.objects.filter(email=user.id).first()  # Get verification data
    
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        
        # Update user details
        user.username = username
        user.phone = phone
        user.email = email
        
        try:
            user.save()  # Save changes to the User table
            
            # Optionally update the photo in UserVerification
            if photo and verification:
                verification.photo = photo
                verification.save()
            
            messages.success(request, "Profile updated successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
        return redirect('profile_page')  # Redirect back to the profile page
    
    context = {
        'user': user,
        'photo': verification.photo.url if verification and verification.photo else None,  # Profile picture
    }
    return render(request, 'profile.html', context)

@login_required
def delete_account(request):
    user = request.user
    user.delete()  # Delete the account
    messages.success(request, "Your account has been deleted.")
    return redirect('login_page')  # Redirect to the home or login page