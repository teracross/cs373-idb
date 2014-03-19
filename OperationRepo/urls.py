from django.conf.urls import patterns, url
from OperationRepo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^business/(\d+)/$', views.business, name='business'),
    url(r'^review/(\d+)/$', views.review, name='review'),
    url(r'^user/(\d+)/$', views.user, name='user'),
)
