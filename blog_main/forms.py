from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'password1','password2']  