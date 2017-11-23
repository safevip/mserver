from django.conf.urls import url
from django.views.generic import TemplateView

from host.views import *

urlpatterns = [
    url(r'^list', HostList.as_view()),
    url(r'^add', HostAdd.as_view()),
    # url(r"^doadd", HostAdd.as_view()),

]