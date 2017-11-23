from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from host.models import Host


# host
class HostList(ListView):
    model = Host
    context_object_name = "hostList"
    template_name = "host/hostlist.html"


class HostAdd:
    pass


########################
# user
class HostUserList:
    pass
