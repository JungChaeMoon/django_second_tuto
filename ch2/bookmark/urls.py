

from django.conf.urls import include, url
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    url('', BookmarkLV.as_view(), name='index'),
    url('(?P<pk>\d+)/$', BookmarkDV.as_view(), name= 'detail'),
]