from django.conf.urls import *
from OperationRepo import views
from OperationRepo import api


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^business/$', views.business_splash, name='business_splash'),
    url(r'^business/(\S+)/$', views.business, name='business'),
    url(r'^review/(\S+)/$', views.review, name='review'),
    url(r'^review/$', views.review_splash, name='review_splash'),
    url(r'^user/(\S+)/$', views.user, name='user'),
    url(r'^user/$', views.user_splash, name='user_splash'),
    url(r'^idb/api/business/$',api.business, name='business_api'),
)