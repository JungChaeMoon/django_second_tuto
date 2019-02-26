from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class PostLV(ListView):
    pass

class PostDV(DetailView):
    pass

class PostAV(ArchiveIndexView):
    pass

class PostYAV(YearArchiveView):
    pass

class PostMAV(MonthArchiveView):
    pass

class PostDAV(DayArchiveView):
    pass

class PostTAV(TodayArchiveView):
    pass

