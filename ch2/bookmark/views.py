# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Bookmark



class BookmarkLV(ListView):
    template_name = 'bookmark/bookmark_list.html'
    model = Bookmark

class BookmarkDV(DetailView):
    template_name = 'bookmark/bookmark_detail.html'
    model = Bookmark