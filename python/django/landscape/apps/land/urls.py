from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^[1-9]$', views.snow),
    url(r'^10$', views.snow),
    url(r'^1[1-9]$', views.desert),
    url(r'^20$', views.desert),
    url(r'^2[1-9]$', views.forest),
    url(r'^30$', views.forest),
    url(r'^3[1-9]$', views.vine),
    url(r'^40$', views.vine),
    url(r'^4[1-9]$', views.trop),
    url(r'^50$', views.trop),
]

# I know what I did wrong, but I'm moving on!!!