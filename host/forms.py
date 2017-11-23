from django import forms
from django.forms import ModelForm

from host.models import Host


# class HostForm(forms.Form):
#     hostname = forms.CharField(label="主机名", max_length=20)
#     address = forms.GenericIPAddressField(label="ip地址")
#


class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['hostname', 'address']
