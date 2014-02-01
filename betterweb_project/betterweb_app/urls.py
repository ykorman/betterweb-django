from django.conf.urls import patterns, url, include
from rest_framework import routers

from betterweb_app import views

# django rest framework quickstart code 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# quickstart end
router.register(r'tips', views.TipViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^withdraw/$', views.withdraw, name='withdraw'),
    url(r'^tip/$', views.tip, name='tip'),
    url(r'^tip/(?P<receiver_uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.tip, name='tip_uuid'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # django rest framework quickstart
)