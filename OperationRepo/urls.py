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
    url(r'^search/$', views.search, name='search'),
    url(r'^api/business/$',api.business_all, name='business_all'),
    url(r'^api/business/(\S+)/$',api.business_id, name='business_id'),
    url(r'^api/business/(\S+)/user$',api.business_id_user, name='business_id_user'),
    url(r'^api/business/(\S+)/review$',api.business_id_review, name='business_id_review'),
    url(r'^api/user/$',api.user_all, name='user_all'),
    url(r'^api/user/(\S+)/$',api.user_id, name='user_id'),
    url(r'^api/user/(\S+)/business$',api.user_id_business, name='user_id_business'),
    url(r'^api/user/(\S+)/review$',api.user_id_review, name='user_id_review'),
    url(r'^api/review/$',api.review_all, name='review_all'),
    url(r'^api/review/(\S+)/$',api.review_id, name='review_id'),
    url(r'^api/review/(\S+)/business$',api.review_id_business, name='review_id_business'),
    url(r'^api/review/(\S+)/user$',api.review_id_user, name='review_id_user'),
    url(r'^apifun/$', views.api_fun, name='api_fun'),
)