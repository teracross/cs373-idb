from django.conf.urls import *
# from tastypie.api import Api
from OperationRepo import views
from OperationRepo import api


# idb_api = Api(api_name='idb')
# idb_api.register(BusinessResource())
# idb_api.register(NeighborhoodsResource())
# idb_api.register(CategoriesResource())
# idb_api.register(AttributesResource())
# idb_api.register(HoursResource())
# idb_api.register(UserResource())
# idb_api.register(User_VotesResource())
# idb_api.register(EliteResource())
# idb_api.register(ComplimentsResource())
# idb_api.register(ReviewResource())
# idb_api.register(Review_VotesResource())

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
    # url(r'^api/', include(idb_api.urls)),
)