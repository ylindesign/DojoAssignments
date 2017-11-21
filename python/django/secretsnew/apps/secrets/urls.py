from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.secrets, name = 'secrets'),
	url(r'^post$', views.post, name = 'post'),
	url(r'^deletepost/(?P<id>\d+)$', views.deletePost, name = 'deletePost'),
	url(r'^like/(?P<id>\d+)$', views.like, name = 'like'),
	url(r'^popular$', views.popular, name = 'popular'),
]