from django.contrib.auth.models import *
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from OperationRepo.models import *
import copy

class BusinessResource(ModelResource):

	class Meta:
		queryset = Business.objects.all()
		resource_name = 'business'
		include_resource_uri = False
		authorization= Authorization()

	def alter_list_data_to_serialize(self, request, business_dict):
		if isinstance(business_dict, dict):
			if 'meta' in business_dict:
				del(business_dict['meta'])
		return business_dict['objects']

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
		include_resource_uri = False
		authorization= Authorization()

	def alter_list_data_to_serialize(self, request, user_dict):
		if isinstance(user_dict, dict):
			if 'meta' in user_dict:
				del(user_dict['meta'])
		return user_dict['objects']

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
	business_id = fields.ForeignKey(BusinessResource, 'business_id')
	user_id = fields.ForeignKey(UserResource, 'user_id')


	class Meta:
		queryset = Review.objects.all()
		resource_name = 'review'
		include_resource_uri = False
		authorization= Authorization()

	def alter_list_data_to_serialize(self, request, review_dict):
		if isinstance(review_dict, dict):
			if 'meta' in review_dict:
				del(review_dict['meta'])
		return review_dict['objects']

class Review_VotesResource(ModelResource):
	review = fields.ForeignKey(ReviewResource, 'review')

	class Meta:
		queryset = Review_Votes.objects.all()
		resource_name = 'review_votes'
		excludes = ["business:", "user", "username", "resource_uri"]


