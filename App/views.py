from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, "Login.html")

def SignUp(request):
    return render(request, "SignUp.html")

def IDVerification(request):
    return render(request, "IDVerification.html")