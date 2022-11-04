from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

PRODUCT_FLAG = (
    ('New', 'New'),
    ('Feature', 'Feature'),
    ('Sale', 'Sale')
)

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='products')
    price = models.FloatField(_("Price"))
    sku = models.IntegerField(_("SKU"))
    tages = TaggableManager()
    desc = models.TextField(_("Description"), max_length=10000)
    flag = models.CharField(_("Flag"), max_length=10, choices=PRODUCT_FLAG)
    subtitle = models.TextField(_("Sub-title"), max_length=500)
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"), related_name='product_brand', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey("Category", verbose_name=_("Category"), related_name='product_category', on_delete=models.SET_NULL, null=True, blank=True)
    video_url = models.URLField(_("Video"), null=True, blank=True)
    quantity = models.IntegerField(_("Quantity"), default=50)

    def __str__(self):
        return self.name




class productImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("productImages"), on_delete=models.CASCADE)
    image = models.ImageField(_("Images"), upload_to='images')

    def __str__(self):
        return str(self.product)
    
        

class Category(models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    image = models.ImageField(_("Image"), upload_to='category')
    
    def __str__(self):
        return self.name
    


class Brand(models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    image = models.ImageField(_("Image"), upload_to='brands')

    def __str__(self):
        return self.name
    


class productReviews(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user_review"), on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("productReviews"), related_name='product_review', on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.IntegerField(_("Rate"))
    review = models.CharField(_("review"), max_length=500)
    created_at = models.DateTimeField(_("create at"), default=timezone.now)

    def __str__(self):
        return str(self.product)