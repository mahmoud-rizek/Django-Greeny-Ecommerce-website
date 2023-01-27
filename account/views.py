from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from products import models as product_models
from orders import models as order_models
# Create your views here.

from .forms import SignupForm, UserActivationForm
from .models import Profile, UserAddrees, userPhoneNumber
from settings.models import Company
from .tasks import print_wellcome


def user_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    user_phone = userPhoneNumber.objects.filter(user=request.user)
    user_addrees = UserAddrees.objects.filter(user=request.user)

    return render(request, 'registration/profile.html', {'profile':user_profile, 
    'user_addrees':user_addrees,
    'user_phone':user_phone})


def welcome(request):
    print_wellcome(10)
    

def dashboard(request):
    users = User.objects.all().count()
    products = product_models.Product.objects.all().count()
    reviews = product_models.productReviews.objects.all().count()
    categories = product_models.Category.objects.all().count()
    brands = product_models.Brand.objects.all().count()
    orders = order_models.Order.objects.all().count()
    
    company = Company.objects.all()
    receved_orders = order_models.Order.objects.filter(status='receved').count()
    processed_orders = order_models.Order.objects.filter(status='processed').count()
    shiped_orders = order_models.Order.objects.filter(status='shiped').count()
    delivered_orders = order_models.Order.objects.filter(status='delivered').count()
  
    return render(request, 'account/dashboard.html', {
        'user':users,
        'company':company,
        'products':products,
        'reviews':reviews,
        'categories':categories,
        'brands':brands,
        'orders':orders,
        'receved_orders':receved_orders,
        'processed_orders':processed_orders,
        'shiped_orders':shiped_orders,
        'delivered_orders':delivered_orders,
    })

    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("Error is at here, after SignupForm !!!!!!!!!")
        if form.is_valid():
            print("Error is at here, after is_valid !!!!!!!!!")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save()
            profile = Profile.objects.get(user__username=username)  
            profile.active = False
            profile.save()
            

            # send email
            send_mail(
                subject= 'Greeny Activate Your Account',
                message=f"user this code {profile.code} to activate your acount", 
                from_email='mahmoudtino56@gmail.com', 
                recipient_list= [email],
                fail_silently=False
            )
            return redirect(f"/accounts/{username}/activate")

    else:
        form = SignupForm()
        print("Error is at here, after else condition !!!!!!!!!")
    return render(request, 'registration/signup.html', {"form":form} )


    

def user_activate(request):

    # profile = Profile.objects.get(user__username=username)  
    
    # if request.method=="POST":
    #     form = UserActivationForm(request.POST)
    #     if form.is_valid():
    #         code = form.cleaned_data["code"]
    #         if profile.code == code :
    #             profile.code_used = True
    #             profile.code = ''
    #             profile.active = True
    #             return redirect("accounts/login")
    #     else:
    #         form= UserActivationForm()
    #     return render(request, 'registration/activate.html', {'form':form})
    # else:
            # form= UserActivationForm()
    return render(request, 'registration/activate.html')