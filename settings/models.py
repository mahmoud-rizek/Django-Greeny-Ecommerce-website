from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=85)
    logo = models.ImageField(_("Company Logo"), upload_to='logo/')
    sub_title = models.CharField(_("About Company"), max_length=500)
    tw_link = models.URLField(_("Tweiter"))
    lk_in_link = models.URLField(_("Linked in"))
    fb_link = models.URLField(_("FaceBook"))
    ista_link = models.URLField(_("Istagram"))
    Addrees = models.TextField(_("Company Addrees"), max_length=100)
    Cphone = models.TextField(_("Company Phone"), max_length=100)
    email = models.TextField(_("Company email"), max_length=100)
    call_us = models.CharField(_("Company Number"), max_length=50)
    email_us = models.EmailField(_("Company Email"), max_length=254)


    def __str__(self):
        return self.name
    