# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.shortcuts import redirect
# Create your views here.

def test(request):
    return redirect("/admin/")

class Index(TemplateView):
    template_name = "index.html"
