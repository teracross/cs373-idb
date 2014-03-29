from django.conf.urls import patterns, url
from OperationRepo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^business/(\S+)/$', views.business, name='business'),
    url(r'^review/(\S+)/$', views.review, name='review'),
    url(r'^user/(\S+)/$', views.user, name='user'),
)
