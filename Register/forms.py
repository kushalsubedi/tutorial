from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # def validate(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email is already registered')
    #     return email
    
    # def validate_pw(self):
    #     pw1 = self.cleaned_data.get('password1')
    #     pw2 = self.cleaned_data.get('password2')
    #     if pw1 != pw2:
    #         raise forms.ValidationError('Passwords do not match')
    #     return pw1
    

