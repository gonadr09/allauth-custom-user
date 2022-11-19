from django import forms
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class SignupForm(forms.Form):
    first_name = forms.CharField(label=_('first name'), max_length=30, required=True)
    last_name = forms.CharField(label=_('last name'), max_length=30, required=True)
    birthday = forms.DateField(label=_("birthday"))
    address = forms.CharField(label=_("address"), max_length=1024,)
    zip_code = forms.CharField(label=_("zip code"), max_length=12,)
    city = forms.CharField(label=_("city"), max_length=1024,)
    country = forms.CharField(label=_("country"), max_length=1024,)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']
        user.address = self.cleaned_data['address']
        user.zip_code = self.cleaned_data['zip_code']
        user.city = self.cleaned_data['city']
        user.country = self.cleaned_data['country']
        user.save()

