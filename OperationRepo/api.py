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
    return HttpResponse(list(Business.objects.filter(business_id=business_id).values()))

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
    return HttpResponse(list(User.objects.filter(user_id=user_id).values()))

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

# # Reviews
# def review(request, *z):
#     context = RequestContext(request)
#     reviewID = z[0]
#     review = get_object_or_404(Review, review_id=reviewID)
#     review_votes_list = Review_Votes.objects.filter(review=review)
#     return render_to_response('OperationRepo/review.html', {"Review":review, "Review_Votes_List":review_votes_list},context)

# # Reviews
# def user(request, *z):
#     context = RequestContext(request)
#     userID = z[0]
#     user = get_object_or_404(User, user_id=userID)
#     user_votes_list = User_Votes.objects.filter(user=user)
#     elite_list = Elite.objects.filter(user=user)
#     compliments_list = Compliments.objects.filter(user=user)

#     return render_to_response('OperationRepo/user.html', 
#         {"User" : user, "User_Votes_List": user_votes_list, 
#         "Elite_List":elite_list, "Compliments_List":compliments_list},context)

# def business_splash (request):
#     context = RequestContext(request)
#     allBusinesses = Business.objects.all()
#     businesses = {}
#     for b in allBusinesses :
#         businesses[str(b.name)] = b.business_id

#     return render_to_response('OperationRepo/business_splash.html', {"bdict": businesses},context)

# def review_splash (request):
#     context = RequestContext(request)
#     allReviews = Review.objects.all().order_by("-date")
#     avgInfo = allReviews.aggregate(Avg('stars'))
#     return render_to_response('OperationRepo/review_splash.html', {"rdict": allReviews, "avgInfo" : avgInfo},context)

# def user_splash (request):
#     context = RequestContext(request)
#     allUsers = User.objects.all()

#     return render_to_response('OperationRepo/user_splash.html', {"userList": allUsers},context)

def toJSstr(a):
    val = str(a).replace("'","\"").replace("True","true").replace("False","false")
    return val
