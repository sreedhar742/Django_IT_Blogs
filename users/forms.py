from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
        
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image_data']  # Change 'image' to 'image_data'

#     def save(self, *args, **kwargs):
#         profile = super().save(commit=False)
#         if self.cleaned_data['image_data']:
#             # Read the uploaded image as bytes
#             image_file = self.cleaned_data['image_data']
#             profile.image_data = image_file.read()
#         profile.save()
#         return profile
