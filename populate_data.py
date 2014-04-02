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
#def populate_user():

#def populate_review():

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
    populate_business()