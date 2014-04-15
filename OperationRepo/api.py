from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json


BUSINESS_FK = ['neighborhoods','categories','attributes','hours']
USER_FK = ['votes','elite','compliments']
REVIEW_FK = ['votes']


# Businesses
@api_view(['GET', 'POST'])
def business_all(request):

    if request.method == 'GET':
        return Response(list(Business.objects.all().values('business_id','name', 'city')))

    elif request.method == 'POST':
        business_json = request.DATA.copy()
        business_json.pop('type',None)
        categories = business_json.pop('categories', None)
        attributes = business_json.pop('attributes', None)
        hours = business_json.pop('hours', None)
        business_json['is_open'] = business_json.pop('open', None)
        b = Business(**business_json)

        if not b:
            return Response("nope", status=status.HTTP_400_BAD_REQUEST)

        b.save()

        for name in categories:
            Categories(business=b, name=name).save()
        for key,value in attributes.items():
            Attributes(business=b, name=key,value=str(value)).save()
        for day,hour in hours.items():
            Hours(business=b,day_of_week=day,open_hour=hour['open'],close_hour=hour['close']).save()

        return Response(request.DATA, status=status.HTTP_201_CREATED)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def business_id(request, business_id):
    
    business = get_object_or_404(Business, business_id=business_id)
    if request.method == 'GET':
        business.__dict__.pop('_state')

        attr = {}
        for attribute in Attributes.objects.filter(business=business).values():
            s = attribute['name'].replace(' ', '_').replace('-','').lower()
            if "{" in str(attribute['value']) :
                attr[s] = toJS(attribute['value'])
            else:
                attr[s] = attribute['value']
            
        business.__dict__['attributes'] = attr
        business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"

        return Response(business.__dict__)
    elif request.method == 'PUT':

        Categories.objects.filter(business=business).delete()
<<<<<<< HEAD
        for name in request.DATA['categories']:
            Categories(business=business, name=name).save()
        for key,value in request.DATA['attributes'].items():
            Attributes(business=business, name=key,value=str(value)).save()
        for day,hour in request.DATA['hours'].items():
            Hours(business=business,day_of_week=day,open_hour=hour['open'],close_hour=hour['close']).save()

        for k in request.DATA:
            if k not in BUSINESS_FK:
                business.__dict__[k] = request.DATA[k]

        attr = {}
        for attribute in Attributes.objects.filter(business=business).values():
            s = attribute['name'].replace(' ', '_').replace('-','').lower()
            if "{" in str(attribute['value']) :
                attr[s] = toJS(attribute['value'])
            else:
                attr[s] = attribute['value']
            
        business.__dict__['attributes'] = attr
        business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"

        business.save()
        business.__dict__.pop('_state',None)
        return Response(business.__dict__,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        Categories.filter(business_id = business_id).delete()
        Attributes.filter(business_id = business_id).delete()
        Hours.filter(business_id = business_id).delete()
        Business.objects.filter(business_id = business_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def business_id_user(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.user.__dict__.pop('_state')
        review.user.__dict__['yelping_since'] = str(review.user.__dict__['yelping_since'])
        review.user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=review.user).values()}
        review.user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=review.user).values()]
        review.user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=review.user).values()}
        review.user.__dict__['type'] = "user"
    users = [review.user.__dict__ for review in reviews]

    return Response(users)

@api_view(['GET'])
def business_id_review(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['type'] = "review"
        
    return Response([review.__dict__ for review in reviews])


# Users
@api_view(['GET', 'POST'])
def user_all(request):

    if request.method == 'GET':
        return Response(list(User.objects.all().values('user_id','name')))

    elif request.method == 'POST':
        user_json = request.DATA.copy()
        user_json.pop('type', None)
        votes = user_json.pop('votes',None)
        elite = user_json.pop('elite',None)
        compliments =  user_json.pop('compliments',None)

        u = User(**user_json)

        if not u:
            return Response("nope", status=status.HTTP_400_BAD_REQUEST)

        u.save()

        for kind,number in votes.items():
            User_Votes(user=u, vote_type=kind,count=number).save()
        for leet in elite:
            Elite(user=u,years_elite=leet).save()
        for kind,number in compliments.items():
            Compliments(user=u,complement_type=kind,num_compliments_of_this_type=number).save()    
        
        return Response(request.DATA, status=status.HTTP_201_CREATED)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_id(request, user_id):
    user = get_object_or_404(User, user_id=user_id)

    if request.method == 'GET':
        user.__dict__.pop('_state')
        user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
        user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
        user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
        user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
        user.__dict__['type'] = "user"

        return Response(user.__dict__)

    elif request.method == 'PUT':

        Elite.objects.filter(user=user).delete()
        for kind,number in request.DATA['votes'].items():
            User_Votes(user=user, vote_type=kind,count=number).save()
        for leet in request.DATA['elite']:
            Elite(user=user,years_elite=leet).save()
        for kind,number in request.DATA['compliments'].items():
            Compliments(user=user,complement_type=kind,num_compliments_of_this_type=number).save()

        for k in request.DATA:
            if k not in USER_FK:
                user.__dict__[k] = request.DATA[k]

        user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
        user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
        user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
        user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
        user.__dict__['type'] = "user"

        user.save()
        user.__dict__.pop('_state',None)

        return Response(user.__dict__,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        User_Votes.objects.filter(user_id = user_id).delete()
        Elite.objects.filter(user_id = user_id).delete()
        Compliments.objects.filter(user_id = user_id).delete()
        User.objects.filter(user_id = user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  



@api_view(['GET'])
def user_id_business(request, user_id):
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
        
        business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"

    return Response([business.__dict__ for business in businesses])

@api_view(['GET'])
def user_id_review(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['type'] = "review"

    return Response([review.__dict__ for review in reviews])


# Reviews
@api_view(['GET', 'POST'])
def review_all(request):

    if request.method == 'GET':
        return Response(list(Review.objects.all().values('review_id','business_id','user_id')))


    elif request.method == 'POST':
        review_json = request.DATA.copy()
        review_json.pop('type',None)
        votes = review_json.pop('votes',None)

        r = Review(**review_json)

        if not r:
            return Response("nope", status=status.HTTP_400_BAD_REQUEST)

        r.save()

        for kind,number in votes.items():
            Review_Votes(review=r, vote_type=kind,count=number).save()
            
        return Response(request.DATA, status=status.HTTP_201_CREATED)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_id(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)

    if request.method == 'GET':
        review.__dict__.pop('_state')
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"
        return Response(review.__dict__)

    elif request.method == 'PUT':

        for kind,number in request.DATA['votes'].items():
            Review_Votes(review=review, vote_type=kind,count=number).save()

        for k in request.DATA:
            if k not in REVIEW_FK:
                review.__dict__[k] = request.DATA[k]

        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"

        review.save()
        review.__dict__.pop('_state',None)

        return Response(review.__dict__,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        Review_Votes.filter(review_id = review_id).delete()
        Review.objects.filter(review_id = review_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def review_id_business(request, review_id):
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
    business.__dict__['categories'] = [c['name'] for c in Categories.objects.filter(business=business).values()]
    business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
    business.__dict__['type'] = "business"
    return Response([business.__dict__])

@api_view(['GET'])
def review_id_user(request, review_id):
    user = get_object_or_404(Review, review_id=review_id).user
    user.__dict__.pop('_state')
    user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
    user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
    user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
    user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
    user.__dict__['type'] = "user"
    return Response([user.__dict__])

def toJS(a):
    val = str(a).replace("'","\"").replace("True","true").replace("False","false")
    return json.loads(val)
