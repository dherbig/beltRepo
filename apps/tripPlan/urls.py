from django.conf.urls import url
from . import views
# ^ So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'destination/(?P<id>\d+)', views.tripInfo, name='tripInfo'),
	url(r'add', views.addTrip, name='addTrip'),
	url(r'confirm', views.confirm, name='confirm'),
	url(r'join/(?P<id>\d+)', views.joinTrip, name='joinTrip')
]
