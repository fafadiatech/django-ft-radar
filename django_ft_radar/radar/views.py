# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from .mixins import BaseContextMixin

class IndexView(BaseContextMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CategoryView(BaseContextMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        return context

class CompanyIndexView(BaseContextMixin, TemplateView):
    template_name = "company_index.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyIndexView, self).get_context_data(**kwargs)
        return context
