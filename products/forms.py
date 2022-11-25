from django import forms
from .models import productReviews



class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = productReviews
        fields  = ['rate' , 'review']