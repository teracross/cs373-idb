from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from django.http import HttpResponse
from django.db.models import Avg
import json
from django.core.serializers.json import DjangoJSONEncoder

# Businesses
def get_business_all(request):
    return HttpResponse(json.dumps(list(Business.objects.all().values('business_id','name', 'city'))))

def get_business_id(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    business.__dict__.pop('_state')

    attr = {}
    for attribute in Attributes.objects.filter(business=business).values():
        s = attribute['name'].replace(' ', '_').replace('-','').lower()
        if "{" in str(attribute['value']) :
            attr[s] = toJS(attribute['value'])
        else:
            attr[s] = attribute['value']
        

    business.__dict__['attributes'] = attr
    
    business.__dict__['neighborhoods'] = [c['name'] for c in Neighborhoods.objects.filter(business=business).values()]
    business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
    business.__dict__['hours'] = {hour['day_of_week'] : {str(hour['open_hour'])[:-3]:str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
    
    return HttpResponse(json.dumps(business.__dict__))

def get_business_id_user(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.user.__dict__.pop('_state')
        review.user.__dict__['yelping_since'] = str(review.user.__dict__['yelping_since'])

        review.user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=review.user).values()}

        review.user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=review.user).values()]
        review.user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=review.user).values()}
    users = [review.user.__dict__ for review in reviews]

    return HttpResponse(json.dumps(users))

def get_business_id_review(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"
        review.__dict__['date'] = str(review.__dict__['date'])

    reviews_dict = [review.__dict__ for review in reviews]
    return HttpResponse(json.dumps(list(reviews_dict)))

# Users
def get_user_all(request):
    return HttpResponse(json.dumps(list(User.objects.all().values('user_id','name'))))

def get_user_id(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    user.__dict__.pop('_state')
    user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
    user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
    user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
    user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
    return HttpResponse(json.dumps(user.__dict__))

def get_user_id_business(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        review.business.__dict__.pop('_state')
    businesses = [review.business for review in reviews]
    for business in businesses:
        attr = {}
        for attribute in Attributes.objects.filter(business=business).values():
            s = attribute['name'].replace(' ', '_').replace('-','').lower()
            if "{" in str(attribute['value']) :
                attr[s] = toJS(attribute['value'])
            else:
                attr[s] = attribute['value']
        
        business.__dict__['attributes'] = attr
        
        business.__dict__['neighborhoods'] = [c['name'] for c in Neighborhoods.objects.filter(business=business).values()]
        business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
        business.__dict__['hours'] = {hour['day_of_week'] : {str(hour['open_hour'])[:-3]:str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
    return HttpResponse(json.dumps([business.__dict__ for business in businesses]))

def get_user_id_review(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"
        review.__dict__['date'] = str(review.__dict__['date'])

    reviews_dict = [review.__dict__ for review in reviews]
    return HttpResponse(json.dumps(list(reviews_dict)))

# Reviews
def get_review_all(request):
    result =[{'user_id':review['user'], 'review_id':review['review_id'], 'business_id':review['business']} for review in Review.objects.all().values('review_id','user','business')]
    return HttpResponse(json.dumps(result))

def get_review_id(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    review.__dict__.pop('_state')
    review.__dict__['date'] = str(review.__dict__['date'])
    review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
    return HttpResponse(json.dumps(review.__dict__))

def get_review_id_business(request, review_id):
    business = get_object_or_404(Review, review_id=review_id).business
    business.__dict__.pop('_state')
    attr = {}
    for attribute in Attributes.objects.filter(business=business).values():
        s = attribute['name'].replace(' ', '_').replace('-','').lower()
        if "{" in str(attribute['value']) :
            attr[s] = toJS(attribute['value'])
        else:
            attr[s] = attribute['value']
    
    business.__dict__['attributes'] = attr
    
    business.__dict__['neighborhoods'] = [c['name'] for c in Neighborhoods.objects.filter(business=business).values()]
    business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
    business.__dict__['hours'] = {hour['day_of_week'] : {str(hour['open_hour'])[:-3]:str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
    return HttpResponse(json.dumps([business.__dict__]))

def get_review_id_user(request, review_id):
    user = get_object_or_404(Review, review_id=review_id).user
    user.__dict__.pop('_state')
    user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
    user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
    user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
    user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
    return HttpResponse(json.dumps([user.__dict__]))

def toJS(a):
    val = str(a).replace("'","\"").replace("True","true").replace("False","false")
    return json.loads(val)
