from django.contrib.auth.models import *
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from OperationRepo.models import *

class BusinessResource(ModelResource):

	class Meta:
		queryset = Business.objects.all()
		resource_name = 'business'
		authorization= Authorization()
		excludes = ["resource_uri"]

class NeighborhoodsResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business')

	class Meta:
		queryset = Neighborhoods.objects.all()
		resource_name = 'neighborhoods'

class CategoriesResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business')

	class Meta:
		queryset = Categories.objects.all()
		resource_name = 'categories'

class AttributesResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business')

	class Meta:
		queryset = Attributes.objects.all()
		resource_name = 'attributes'

class HoursResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business')

	class Meta:
		queryset = Hours.objects.all()
		resource_name = 'hours'

class UserResource(ModelResource):

	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		authorization= Authorization()

class User_VotesResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = User_Votes.objects.all()
		resource_name = 'user_votes'

class EliteResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = Elite.objects.all()
		resource_name = 'elite'

class ComplimentsResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = Compliments.objects.all()
		resource_name = 'compliments'

class ReviewResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business')
	user = fields.ForeignKey(UserResource, 'user')


	class Meta:
		queryset = Review.objects.all()
		resource_name = 'review'
		authorization= Authorization()

class Review_VotesResource(ModelResource):
	review = fields.ForeignKey(ReviewResource, 'review')

	class Meta:
		queryset = Review_Votes.objects.all()
		resource_name = 'review_votes'
		excludes = ["business:", "user", "username", "resource_uri"]


