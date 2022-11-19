from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

LPRECIOS = [
    ('1', 'Lista 1'),
    ('2', 'Lista 2')
]

class CustomUser(AbstractUser):
    birthday = models.DateField(verbose_name=_("birthday"), blank=True, null=True)
    address = models.CharField(verbose_name=_("address"), max_length=1024, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_("zip code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=_("city"), max_length=1024, blank=True, null=True)
    country = models.CharField(verbose_name=_("country"), max_length=1024, blank=True, null=True)
    price_list = models.CharField(verbose_name=_("price list"), max_length=2, choices=LPRECIOS, default='1')
    
    def __str__(self):
        return f'{self.username}: {self.first_name} {self.last_name}'
