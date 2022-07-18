from django.views.generic import ListView
from django.shortcuts import render

from .models import AddOn


class AddOnActualView(ListView):
    queryset = AddOn.objects.actual()
    template_name = 'addons/actual.html'


class AddOnArchiveView(ListView):
    queryset = AddOn.objects.published()
    template_name = 'addons/archive.html'
