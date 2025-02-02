from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    """
    LoginForm is a Django form for user authentication.

    Fields:
        username (CharField): A text input field for the user's username with a placeholder and CSS classes for styling.
        password (CharField): A password input field for the user's password with a placeholder and CSS classes for styling.
    """
    username=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Your username",
         "class":"w-full py-4 px-4 rounded-xl"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Password", 
        "class":"w-full py-4 px-4 rounded-xl"
    }))

class SignupForm(UserCreationForm):
    """
    SignupForm is a form for user registration that extends the UserCreationForm.
    It includes fields for username, email, password, and password confirmation.
    Attributes:
        username (forms.CharField): A CharField for the username with a TextInput widget.
        email (forms.EmailField): An EmailField for the email with an EmailInput widget.
        password1 (forms.CharField): A CharField for the password with a PasswordInput widget.
        password2 (forms.CharField): A CharField for password confirmation with a PasswordInput widget.
    Meta:
        model (User): The model associated with this form.
        fields (tuple): The fields to include in the form.
    """
    class Meta:
        model=User 
        fields=('username', 'email', 'password1', 'password2')

    username=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Your username",
        "class":"w-full py-4 px-4 rounded-xl"
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder":"Your email",
        "class":"w-full py-4 px-4 rounded-xl"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Your password",
        "class":"w-full py-4 px-4 rounded-xl"
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Repeat password",
        "class":"w-full py-4 px-4 rounded-xl"
    }))

