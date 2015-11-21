from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagereader.feed import views

urlpatterns = [
    url(r'^$', views.list, name='feed_list'),
    url(r'submit', views.submit),
    url(r'view', views.list),
]
