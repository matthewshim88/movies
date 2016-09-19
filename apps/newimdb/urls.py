from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.addMovie),
    url(r'^(?P<id>)\d+/addActor$', views.addActor)
]
