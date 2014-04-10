from django.conf.urls import *
from OperationRepo import views
from OperationRepo.api import *

business_resource = BusinessResource()
user_resource = UserResource()
review_resource = ReviewResource()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^business/$', views.business_splash, name='business_splash'),
    url(r'^business/(\S+)/$', views.business, name='business'),
    url(r'^review/(\S+)/$', views.review, name='review'),
    url(r'^review/$', views.review_splash, name='review_splash'),
    url(r'^user/(\S+)/$', views.user, name='user'),
    url(r'^user/$', views.user_splash, name='user_splash'),
    (r'^api/', include(business_resource.urls)),
    (r'^api/', include(user_resource.urls)),
    (r'^api/', include(review_resource.urls)),
)