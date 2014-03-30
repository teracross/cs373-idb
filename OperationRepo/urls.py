from django.conf.urls import patterns, url
from OperationRepo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^business/(\S+)/$', views.business, name='business'),
    url(r'^business/all/(\d+)/$', views.business_splash, name='business_splash'),
    url(r'^review/(\S+)/$', views.review, name='review'),
    url(r'^review/all/(\d+)/$', views.business_splash, name='review_splash'),
    url(r'^user/(\S+)/$', views.user, name='user'),
    url(r'^user/all/(\d+)/$', views.business_splash, name='user_splash'),
)
