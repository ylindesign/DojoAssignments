from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^process$', views.process, name = 'process'),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'destroy'),
	url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove'),
]