import os
import json

def populate_business():
    business_data = open('business.txt')
    for line in business_data:
        if not ("{" in line):
            continue

        business_json = json.loads(line) 
        business_json.pop('type',None)
        neighborhoods = business_json.pop('neighborhoods', None)
        categories = business_json.pop('categories', None)
        attributes = business_json.pop('attributes', None)
        hours = business_json.pop('hours', None)
        business_json['is_open'] = business_json.pop('open', None)
        b = add_business(business_json)
        for neighborhood in neighborhoods:
            Neighborhood.objects.get_or_create(business=b, name=name)
        for name in categories:
            Categories.objects.get_or_create(business=b, name=name)
        for key,value in attributes.items():
            Attributes.objects.get_or_create(business=b, name=key,value=str(value))
        for day,hour in hours.items():
            Hours.objects.get_or_create(business=b,day_of_week=day,open_hour=hour['open'],close_hour=hour['close'])

    business_data.close()

def populate_user():
    user_data = open('user.txt')
    for line in user_data:
        if not ("{" in line):
            continue

        user_json = json.loads(line) 
        user_json.pop('type',None)
        
        user_Votes = user_json.pop('votes', None)
        friends = user_json.pop('friends', None)
        compliments = user_json.pop('compliments', None)
        elite = user_json.pop('elite', None)
        user_json['yelping_since'] = user_json['yelping_since'] + "-01"

        u = add_user(user_json)

        for key,value in user_Votes.items():
            User_Votes.objects.get_or_create(user=u, vote_type=key,count=value)
        for friend_id in friends:
            Friends.objects.get_or_create(user=u, friend_id=friend_id)
        for key,value in compliments.items():
            Compliments.objects.get_or_create(user=u, complement_type=key,num_compliments_of_this_type=value)
        for years_elite in elite:
            Elite.objects.get_or_create(user=u, years_elite=years_elite)
    user_data.close()

def populate_review():
    review_data = open('review.txt')
    for line in review_data:
        if not ("{" in line):
            continue

        review_json = json.loads(line) 
        review_json.pop('type',None)
        user_id = review_json.pop('user_id',None)
        business_id = review_json.pop('business_id',None)
        review_Votes = review_json.pop('votes', None)
        
        review_json['business']=Business.objects.get(business_id=business_id)
        review_json['user']=User.objects.get(user_id=user_id)

        print("business_id: " + business_id)
        print("user_id: " + user_id)
        print("review_id: " + review_json['review_id'])
        r = add_review(review_json)

        for key,value in review_Votes.items():
            Review_Votes.objects.get_or_create(review=r, vote_type=key,count=value)
        
    review_data.close()

def add_business(stuffs):
    b = Business.objects.get_or_create(**stuffs)[0]
    return b

def add_user(stuffs):
    u = User.objects.get_or_create(**stuffs)[0]
    return u

def add_review(stuffs):
    r = Review.objects.get_or_create(**stuffs)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idb.settings')
    from OperationRepo.models import *
    #populate_business()
    #print("populated businesses")
    #populate_user()
    #print("populated users")
    populate_review()
    print("populated reviews")