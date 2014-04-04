from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from django.http import HttpResponse
from django.db.models import Avg
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# def index(request):
#     # Request the context of the request.
#     # The context contains information such as the client's machine details, for example.
#     context = RequestContext(request)
#     context_dict = {'message': "Hello World"}
#     return render_to_response('OperationRepo/index.html', context_dict, context)


# Businesses
def get_business_all(request):
    return HttpResponse(json.dumps(list(Business.objects.all().values('business_id','name'))))

def get_business_id(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    business.__dict__.pop('_state')
    return HttpResponse(json.dumps(business.__dict__))

def get_business_id_user(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.user.__dict__.pop('_state')
        review.user.__dict__['yelping_since'] = str(review.user.__dict__['yelping_since'])
    users = [review.user.__dict__ for review in reviews]
    return HttpResponse(json.dumps(users))

def get_business_id_review(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    return HttpResponse(json.dumps(list(Review.objects.filter(business=business).values()),cls=DjangoJSONEncoder))

# Users
def get_user_all(request):
    return HttpResponse(json.dumps(list(User.objects.all().values('user_id','name'))))

def get_user_id(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    user.__dict__.pop('_state')
    user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
    return HttpResponse(json.dumps(user.__dict__))

def get_user_id_business(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        review.business.__dict__.pop('_state')
    business = [review.business.__dict__ for review in reviews]
    return HttpResponse(json.dumps(business))
def get_user_id_review(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    return HttpResponse(json.dumps(list(Review.objects.filter(user=user).values()),cls=DjangoJSONEncoder))

# Reviews
def get_review_all(request):
    result =[{'user_id':review['user'], 'review_id':review['review_id'], 'business_id':review['business']} for review in Review.objects.all().values('review_id','user','business')]
    return HttpResponse(json.dumps(result))

def get_review_id(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    review.__dict__.pop('_state')
    review.__dict__['date'] = str(review.__dict__['date'])
    return HttpResponse(json.dumps(review.__dict__))

def get_review_id_business(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    review.business.__dict__.pop('_state')
    return HttpResponse(json.dumps(review.business.__dict__))

def get_review_id_user(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    review.user.__dict__.pop('_state')
    review.user.__dict__['yelping_since'] = str(review.user.__dict__['yelping_since'])
    return HttpResponse(json.dumps(review.user.__dict__))