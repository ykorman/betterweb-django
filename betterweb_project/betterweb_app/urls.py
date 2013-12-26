from django.conf.urls import patterns, url

from betterweb_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'betterweb_app/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'betterweb_app/logout.html'}),
    url(r'^(?P<username>\w+)/$', views.landing, name='landing'),
    url(r'^(?P<username>\w+)/deposit/$', views.deposit, name='deposit'),
    url(r'^(?P<username>\w+)/withdraw/$', views.withdraw, name='withdraw'),
)