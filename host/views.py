from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.db import connection
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
    def get(self, request):
        ids = request.GET.get("ids")
        # Host.objects.filter()
        if ids.endswith(","):
            ids = ids[:-1]
            idlist = ids.split(",")
        print(idlist)
        with connection.cursor() as cursor:
            cursor.execute("delete from hm_host where id in %s", [idlist])
        return HttpResponseRedirect("/host/list")


class HostEdit(UpdateView):
    pass


########################
# user
class HostUserList:
    pass
