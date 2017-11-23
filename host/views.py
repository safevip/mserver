from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from host.forms import HostForm
from host.models import Host


# host
class HostList(ListView):
    model = Host
    context_object_name = "hostList"
    template_name = "host/hostlist.html"


class HostDetail:
    pass


class HostAdd(CreateView):
    model = Host
    template_name = 'host/hostadd.html'
    success_url = "list"
    form_class = HostForm
    # fields = ['hostname', 'address']


class HostDel(DeleteView):
    pass


class HostEdit(UpdateView):
    pass


########################
# user
class HostUserList:
    pass
