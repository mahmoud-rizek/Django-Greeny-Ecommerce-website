from django.shortcuts import render

# Create your views here.



def add_to_cart(request):
    if request.method == "POST" :
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        

