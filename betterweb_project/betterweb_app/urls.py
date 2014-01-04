from django.conf.urls import patterns, url

from betterweb_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^withdraw/$', views.withdraw, name='withdraw'),
)