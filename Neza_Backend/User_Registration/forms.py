from django import forms
from django.contrib.auth.forms import UserCreationForm
from User_Registration.models import User

class UserUploadForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = "__all__"    