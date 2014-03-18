from django.conf.urls import patterns, url
from OperationRepo import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^business1/', views.business1, name='business1'),
	url(r'^business2/', views.business2, name='business2'),
	url(r'^business3/', views.business3, name='business3'),
	url(r'^review1/', views.review1, name='review1'),
	url(r'^review2/', views.review2, name='review2'),
	url(r'^review3/', views.review3, name='review3'),
	url(r'^user1/', views.user1, name='user1'),
	url(r'^user2/', views.user2, name='user2'),
	url(r'^user3/', views.user3, name='user3'),
)
