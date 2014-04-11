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
    url(r'^api/business/$',api.get_business_all, name='get_business_all'),
    url(r'^api/business/(\S+)/$',api.get_business_id, name='get_business_id'),
    url(r'^api/business/(\S+)/user$',api.get_business_id_user, name='get_business_id_user'),
    url(r'^api/business/(\S+)/review$',api.get_business_id_review, name='get_business_id_review'),
    url(r'^api/user/$',api.get_user_all, name='get_user_all'),
    url(r'^api/user/(\S+)/$',api.get_user_id, name='get_user_id'),
    url(r'^api/user/(\S+)/business$',api.get_user_id_business, name='get_user_id_business'),
    url(r'^api/user/(\S+)/review$',api.get_user_id_review, name='get_user_id_review'),
    url(r'^api/review/$',api.get_review_all, name='get_review_all'),
    url(r'^api/review/(\S+)/$',api.get_review_id, name='get_review_id'),
    url(r'^api/review/(\S+)/business$',api.get_review_id_business, name='get_review_id_business'),
    url(r'^api/review/(\S+)/user$',api.get_review_id_user, name='get_review_id_user'),
)