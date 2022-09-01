from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.

PRODUCT_FLAG = (
    ('New', 'New'),
    ('Feature', 'Feature'),
    ('Sale', 'Sale')
)

class product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='/products', height_field=None, width_field=None, max_length=None)
    price = models.FloatField(_("Price"))
    sku = models.IntegerField(_("SKU"))
    tages = ''
    desc = models.TextField(_("Description"), max_length=10000)
    flag = models.CharField(_("Flag"), max_length=10, choices=PRODUCT_FLAG)
    subtitle = models.TextField(_("Sub-title"), max_length=500)
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"), on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.SET_NULL, null=True, blank=True)
    video_url = models.URLField(_("Video"), null=True, blank=True)


class productImages(models.Model):
    product = models.ForeignKey(product, verbose_name=_("productImages"), on_delete=models.CASCADE)
    image = models.ImageField(_("Images"), upload_to='images')


class productReviews(models.Model):
    user = ''
    product = models.ForeignKey(product, verbose_name=_("productReviews"), related_name='product_review', on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.IntegerField(_("Rate"))
    review = models.CharField(_("review"), max_length=500)
    created_at = models.DateTimeField(_("create at"), default=timezone)


class Category(models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    image = models.ImageField(_("Image"), upload_to='category')


class Brand(models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    image = models.ImageField(_("Image"), upload_to='brands')
