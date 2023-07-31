from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAddrees, userPhoneNumber

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class UserActivationForm(forms.ModelForm):
    code = forms.IntegerField(max_value=8)
    

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = userPhoneNumber
        fields  = ['number' , 'data_type']
        
class UserAddreesForm(forms.ModelForm):
    class Meta:
        model = UserAddrees
        fields = ['country', 'city', 'streat', 'notes', 'region', 'data_type']