from django.db import models

# User Model
class User(models.Model):
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    phone = models.CharField(max_length=13, blank=True, null=True)
    

# User Verification Model 
class UserVerification(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="verifications")
    id_document = models.ImageField(upload_to='id_docs/')
    photo = models.ImageField(upload_to='photos/')
    verified_at = models.DateTimeField(auto_now_add=True)

# Listing Model
class Listing(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Amenities Model
class Amenity(models.Model):
    name = models.CharField(max_length=100)
    listings = models.ManyToManyField(Listing, related_name='amenities')

# Property Photos Model
class PropertyPhoto(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='property_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Booking Model
class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'listing': self.listing.title,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'payment_status': self.payment.status,
            'total_price': str(self.total_price),
        }

# Payment Model
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

# Review Model
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

# Support Ticket Model
class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='open')

# Blacklist Model
class Blacklist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blacklist')
    reason = models.TextField()
    banned_at = models.DateTimeField(auto_now_add=True)

# Security Alerts Model
class SecurityAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='security_alerts')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='security_alerts')
    alert_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

# Geo-Tracking Model
class GeoTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='geo_tracking')
    latitude = models.FloatField()
    longitude = models.FloatField()
    tracked_at = models.DateTimeField(auto_now_add=True)

# Discounts and Promotions Model
class Discount(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='discounts')
    discount_code = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_until = models.DateField()

class Emergency(models.Model):
    keyword = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)