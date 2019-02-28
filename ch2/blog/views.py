from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import *
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from .models import Post
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    template_name = 'blog/post_archive.html'
    make_object_list = True

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    template_name = 'blog/post_archive_year.html'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    template_name = 'blog/post_archive_month.html'
    date_field = 'modify_date'
    make_object_list = True

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'
    template_name = 'blog/post_archive_day.html'
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class SearchFormView(FormView):
    pass