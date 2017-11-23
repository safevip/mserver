from django.conf.urls import url
from host.views import *

urlpatterns = [
    url(r'^list', HostList.as_view()),
]