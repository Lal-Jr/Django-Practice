from django.conf.urls import url
from django.urls.resolvers import url
from secondApp import views

urlpattern = [
    url(r'^$', views.help, name='help'),
]

