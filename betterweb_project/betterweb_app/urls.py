from django.conf.urls import patterns, url, include

from betterweb_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^withdraw/$', views.withdraw, name='withdraw'),
    url(r'^tip/$', views.tip, name='tip'),
    url(r'^tip/(?P<receiver_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.tip, name='tip_uuid'),
)
