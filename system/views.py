from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class SystemMain(TemplateView):
    template_name = 'common/index.html'
