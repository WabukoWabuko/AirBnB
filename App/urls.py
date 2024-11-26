from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="login_page"),
    path('signup/', views.SignUp, name="signup_page"),
    path('verification/', views.IDVerification, name="id_verification_page"),
    path('2FA', views.otherVerification, name="other_verification_ways_page"),
]
