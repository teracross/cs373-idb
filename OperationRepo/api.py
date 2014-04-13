from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json

# Businesses
@api_view(['GET', 'POST'])
def get_business_all(request):
    if request.method == 'GET':
        return Response(list(Business.objects.all().values('business_id','name', 'city')))

    elif request.method == 'POST':
        business_json = request.DATA
        business_json.pop('type',None)
        neighborhoods = business_json.pop('neighborhoods', None)
        categories = business_json.pop('categories', None)
        attributes = business_json.pop('attributes', None)
        hours = business_json.pop('hours', None)
        business_json['is_open'] = business_json.pop('open', None)
        b = Business(**business_json)

        if not b:
            return Response("nope", status=status.HTTP_400_BAD_REQUEST)

        b.save()

        for neighborhood in neighborhoods:
            Neighborhood(business=b, name=name).save()
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
def get_business_id(request, business_id):
    
    business = get_object_or_404(Business, business_id=business_id)
    #business.__dict__.pop('_state')
    if request.method == 'GET':
        #business = get_object_or_404(Business, business_id=business_id)
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
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"

        return Response(business.__dict__)
    elif request.method == 'PUT':
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
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"
        diff = [v for v in request.DATA if request.DATA[v] != business.__dict__[v]]
        #need to create new subkeys if they don't currently exist
        for v in diff:
            #works for none nested attributes
            business.__dict__[v] = request.DATA[v]
        business.save()
        return Response(request.DATA,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        Business.objects.filter(business_id = business_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def get_business_id_user(request, business_id):
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
def get_business_id_review(request, business_id):
    business = get_object_or_404(Business, business_id=business_id)
    reviews = Review.objects.filter(business=business)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['type'] = "review"
        

    reviews_dict = [review.__dict__ for review in reviews]
    return Response(list(reviews_dict))

# Users
@api_view(['GET', 'POST'])
def get_user_all(request):

    if request.method == 'GET':
        return Response(list(User.objects.all().values('user_id','name')))

    elif request.method == 'POST':
        user_json = request.DATA
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
            Compliments(user=u,complement_type=kind,num_compliments=number).save()    
        
        return Response(request.DATA, status=status.HTTP_201_CREATED)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_user_id(request, user_id):
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

        user.__dict__['yelping_since'] = str(user.__dict__['yelping_since'])
        user.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in User_Votes.objects.filter(user=user).values()}
        user.__dict__['elite'] = [el['years_elite'] for el in Elite.objects.filter(user=user).values()]
        user.__dict__['compliments'] ={compliment['complement_type']:compliment['num_compliments_of_this_type'] for compliment in Compliments.objects.filter(user=user).values()}
        user.__dict__['type'] = "user"

        diff = [v for v in request.DATA if request.DATA[v] != user.__dict__[v]]
        #need to create new subkeys if they don't currently exist
        for v in diff:
            #works for none nested attributes
            user.__dict__[v] = request.DATA[v]
        user.save()

        return Response(request.DATA,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        User.objects.filter(user_id = user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  



@api_view(['GET'])
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
        business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
        business.__dict__['type'] = "business"
    return Response([business.__dict__ for business in businesses])

@api_view(['GET'])
def get_user_id_review(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        review.__dict__.pop('_state')
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['type'] = "review"

    reviews_dict = [review.__dict__ for review in reviews]
    return Response(list(reviews_dict))

# Reviews
@api_view(['GET', 'POST'])
def get_review_all(request):

    if request.method == 'GET':
        return Response(list(Review.objects.all().values('review_id','business_id','user_id')))
    #result =[{'user_id':review['user'], 'review_id':review['review_id'], 'business_id':review['business']} for review in Review.objects.all().values('review_id','user','business')]
    #return Response(result)

    elif request.method == 'POST':
        review_json = request.DATA
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
def get_review_id(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)

    if request.method == 'GET':
        review.__dict__.pop('_state')
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"
        return Response(review.__dict__)

    elif request.method == 'PUT':
        review.__dict__['date'] = str(review.__dict__['date'])
        review.__dict__['votes'] = {vote['vote_type']:vote['count'] for vote in Review_Votes.objects.filter(review=review).values()}
        review.__dict__['type'] = "review"

        diff = [v for v in request.DATA if request.DATA[v] != review.__dict__[v]]
        #need to create new subkeys if they don't currently exist
        for v in diff:
            #works for none nested attributes
            review.__dict__[v] = request.DATA[v]
        review.save()

        return Response(request.DATA,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        Review.objects.filter(review_id = review_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

    else:
        return Response("nope", status=status.HTTP_400_BAD_REQUEST)  






@api_view(['GET'])
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
    business.__dict__['hours'] = {hour['day_of_week'] : {'open':str(hour['open_hour'])[:-3], 'close':str(hour['close_hour'])[:-3]} for hour in Hours.objects.filter(business=business).values()}
    business.__dict__['type'] = "business"
    return Response([business.__dict__])

@api_view(['GET'])
def get_review_id_user(request, review_id):
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

def dict_pop(dict, subkeys):
    pass
