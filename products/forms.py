from django import forms
from .models import productReviews



class formReviews(forms.ModelForm):
    class Meta:
        model = productReviews
        fields  = ['rate' , 'review']