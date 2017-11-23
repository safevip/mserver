from django.conf.urls import url
from host.views import *
from system.views import SystemMain

urlpatterns = [
    url(r'^main', SystemMain.as_view()),
]