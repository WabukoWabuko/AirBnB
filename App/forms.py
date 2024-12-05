from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Login", css_class="btn-primary w-100"))
    
    class Meta:
        model = User
        fields = ['email', 'password']


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label="Full Name",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Sign Up", css_class="btn-primary w-100"))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

class MFAForm(forms.Form):
    verification_code = forms.CharField(
        label="Verification Code",
        max_length=6,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter code",
                "maxlength": 6,
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Verify", css_class="btn-primary w-100"))

class IdentityVerificationForm(forms.Form):
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "1234567890",
            }
        ),
    )
    id_card = forms.ImageField(
        label="Upload ID Card (Image)",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*",
            }
        ),
    )
    current_photo = forms.ImageField(
        label="Upload Current Photo",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*",
            }
        ),
    )
    
class AuthenticationCodeForm(forms.Form):
    verification_code = forms.CharField(
        label="Verification Code",
        max_length=6,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter code",
                "maxlength": 6,
                "required": True,
            }
        ),
    )