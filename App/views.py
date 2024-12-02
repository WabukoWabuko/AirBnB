from django.shortcuts import render

# Create your views here.
def Login(request):
    
    return render(request, "Login.html")

def SignUp(request):
    # After clicking the button it should submit and go direct to verification page 
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

def messages(request):
    return render(request, "messages.html")

def payments(request):
    return render(request, "payments.html")

def support(request):
    return render(request, "support.html")

def makeBooking(request):
    return render(request, "makeBooking.html")