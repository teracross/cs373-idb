from django.conf.urls import patterns, url
from OperationRepo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^business/all/$', views.business_splash, name='business_splash'),
    url(r'^business/id/(\S+)/$', views.business, name='business'),
    url(r'^review/id/(\S+)/$', views.review, name='review'),
    url(r'^user/id/(\S+)/$', views.user, name='user'),
)
