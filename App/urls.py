from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from .views import emergency_alert

urlpatterns = [
    
    path('', views.Index, name="index_page"),
    path('logout/', views.Logout, name="logout_page"),
    path('login/', views.Login, name="login_page"),
    path('signup/', views.SignUp, name="signup_page"),
    path('verification/', views.IDVerification, name="id_verification_page"),
    path('2FA/', views.otherVerification, name="other_verification_ways_page"),
    path('dashboard/', views.dashboard, name="dashboard_page"),
    path('bookings/', views.bookings, name="bookings_page"),
    path('faq/', views.faq, name="faq_page"),
    path('feedback/', views.feedback, name="feedback_page"),
    path('listings/', views.listings, name="listings_page"),
    path('messagesM/', views.messagesM, name="messages_page"),
    path('payments/', views.payments, name="payments_page"),
    path('support/', views.support, name="support_page"),
    path('make_booking/', views.make_booking, name='make_booking'),
    # path('api/emergency-alert/', emergency_alert, name='emergency_alert'),
    path('emergency/', views.report_emergency, name='report_emergency'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('compose_message/', views.compose_message, name='compose_message'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile, name='profile_page'),
    path('delete_account/', views.delete_account, name='delete_account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
