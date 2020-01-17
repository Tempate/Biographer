from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^search/$', views.search, name="search"),
    url(r'^index/$', views.index, name="index"),
    url(r'^index/category=(?P<category>.+)$', views.index, name="index"),
    url(r'^biography/name=(?P<name>.+)$', views.biography, name="biography"),
]
