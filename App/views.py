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