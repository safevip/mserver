from django.conf.urls import url
from project.views import *

urlpatterns = [
    url(r'^list', ProjectList.as_view()),
    url(r'^add', ProjectAdd.as_view()),
    url(r'^edit', ProjectEdit.as_view()),
    url(r'^task/list', TaskList.as_view()),
]
