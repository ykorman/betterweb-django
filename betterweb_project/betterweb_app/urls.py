from django.conf.urls import patterns, url, include
from rest_framework import routers

from betterweb_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^withdraw/$', views.withdraw, name='withdraw'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)