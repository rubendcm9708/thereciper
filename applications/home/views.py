from django.shortcuts import render

from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = "home/index.html"
