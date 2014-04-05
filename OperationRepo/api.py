from django.contrib.auth.models import *
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from OperationRepo.models import *
import copy
from django.forms.models import model_to_dict
from django.http import HttpResponse


class BusinessResource(ModelResource):

	class Meta:
		queryset = Business.objects.all()
		fields = ['business_id','name','city']
		include_resource_uri = False
		resource_name = 'business'
		authorization= Authorization()

	def dehydrate(self, bundle):
		neighborhoods = Neighborhoods.objects.filter(business=bundle.data['business_id'])
		bundle.data['neigh'] = [model_to_dict(c) for c in neighborhoods]
		bundle.data['neighborhoods'] = [c['name'] for c in bundle.data['neigh']]
		del(bundle.data['neigh'])

		categories = Categories.objects.filter(business=bundle.data['business_id'])
		bundle.data['cat'] = [model_to_dict(c) for c in categories]
		bundle.data['categories'] = [c['name'] for c in bundle.data['cat']]
		del(bundle.data['cat'])
		
		attributes = Attributes.objects.filter(business=bundle.data['business_id'])
		bundle.data['attr'] = [model_to_dict(c) for c in attributes]
		bundle.data['attributes'] = {}
		for v in bundle.data['attr']:
			s = v['name'].replace(' ', '_').replace('-','').lower()
			bundle.data['attributes'][s] = v['value'].replace('False', 'false')	.replace('True','true')		
		del(bundle.data['attr'])

		hours = Hours.objects.filter(business=bundle.data['business_id'])
		bundle.data['hrs'] = [model_to_dict(c) for c in hours]
		bundle.data['hours'] = {}
		for v in bundle.data['hrs']:
			temp = {}
			temp['close'] = v['close_hour']
			temp['open'] = v['open_hour']
			bundle.data['hours'][v['day_of_week']] = temp
		del(bundle.data['hrs'])
		return bundle

	def alter_list_data_to_serialize(self, request, business_dict):
		if isinstance(business_dict, dict):
			if 'meta' in business_dict:
				del(business_dict['meta'])
		return business_dict['objects']


class NeighborhoodsResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business', full=True)

	class Meta:
		queryset = Neighborhoods.objects.all()
		resource_name = 'neighborhoods'


class CategoriesResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business', full=True)

	class Meta:
		queryset = Categories.objects.all()
		resource_name = 'categories'


class AttributesResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business', full=True)

	class Meta:
		queryset = Attributes.objects.all()
		resource_name = 'attributes'
		filtering = {
			'business': ALL_WITH_RELATIONS
		}

class HoursResource(ModelResource):
	business = fields.ForeignKey(BusinessResource, 'business', full=True)

	class Meta:
		queryset = Hours.objects.all()
		resource_name = 'hours'
		filtering = {
			'business': ALL_WITH_RELATIONS
		}

class UserResource(ModelResource):

	class Meta:
		queryset = User.objects.all()
		fields = ['user_id','name']
		include_resource_uri = False
		authorization= Authorization()

	def dehydrate(self, bundle):
		user_votes = User_Votes.objects.filter(user=bundle.data['user_id'])
		bundle.data['uv'] = [model_to_dict(c) for c in user_votes]
		bundle.data['votes'] = {}		
		for v in bundle.data['uv']:
			bundle.data['votes'][v['vote_type']] = v['count']
		del(bundle.data['uv'])

		elite = Elite.objects.filter(user=bundle.data['user_id'])
		bundle.data['el'] = [model_to_dict(c) for c in elite]
		for v in bundle.data['el']:
			bundle.data['elite'] = v['years_elite']
		del(bundle.data['el'])

		compliments = Compliments.objects.filter(user=bundle.data['user_id'])
		bundle.data['comp'] = [model_to_dict(c) for c in compliments]
		bundle.data['compliments'] = {}		
		for v in bundle.data['comp']:
			bundle.data['compliments'][v['complement_type']] = v['num_compliments_of_this_type']
		del(bundle.data['comp'])

		return bundle

	def alter_list_data_to_serialize(self, request, user_dict):
		if isinstance(user_dict, dict):
			if 'meta' in user_dict:
				del(user_dict['meta'])
		return user_dict['objects']

class User_VotesResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user', full=True)

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
		#fields = ['review_id','business_id','user_id']
		include_resource_uri = False
		authorization= Authorization()

	def dehydrate(self, bundle):
		review_votes = Review_Votes.objects.filter(review=bundle.data['review_id'])
		bundle.data['rv'] = [model_to_dict(c) for c in review_votes]
		bundle.data['votes'] = {}		
		for v in bundle.data['rv']:
			bundle.data['votes'][v['vote_type']] = v['count']
		del(bundle.data['rv'])
		return bundle

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

"""
class BusinessReviewResource(ModelResource):
	reviews = fields.ToManyField(ReviewResource, 'reviews', full=True)
	def prepend_urls(self):
		return [
		#(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/reviews%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_review'), name="api_get_review"),
		]

	def get_review(self, request, **kwargs):
		try:
			bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
			obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
		except ObjectDoesNotExist:
			return HttpGone()
		except MultipleObjectsReturned:
			return HttpMultipleChoices("More than one resource is found at this URI.")

			review_resource = ReviewResource()
			return review_resource.get_detail(request, parent_id=obj.pk)
"""

