from django import forms
from django.db import IntegrityError

from ..repository.user_repository import filter_by

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Form's extra validations
        if filter_by(username=username).exists():
            error_message: str = "This username is already taken."
            self.add_error("username", error_message)
            raise forms.ValidationError(error_message)

        if filter_by(email=email).exists():
            error_message: str = "This email is already registered."
            self.add_error("email", error_message)
            raise forms.ValidationError(error_message)

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
            raise forms.ValidationError("Passwords do not match.")
        


        return cleaned_data
