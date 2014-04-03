from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from OperationRepo.models import *
from django.http import HttpResponse
import json

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {'message': "Hello World"}
    return render_to_response('OperationRepo/index.html', context_dict, context)


# Businesses
def business(request, *z):
    context = RequestContext(request)
    businessID = z[0]
    thebusiness = Business.objects.get(business_id=str(businessID))
    thereviews = Review.objects.filter(business_id=str(businessID))

    theAttributesList = Attributes.objects.filter(business=thebusiness)
    multiAtrributesDict = {}
    singleAttributesDict = {}
    for objects in theAttributesList :
        if "{" in str(objects.value):
            multiAtrributesDict[objects.name] = toJS(objects.value)
        else :
            singleAttributesDict[objects.name] = objects.value

    theCategoriesList = Categories.objects.filter(business=thebusiness)


    return render_to_response('OperationRepo/business.html', {"Business" : thebusiness,
                                                            "Reviews":thereviews,
                                                            # "ReviewsArray":thereviews,
                                                            "MultiValueAttributes":multiAtrributesDict,
                                                            "SingleValueAttributes":singleAttributesDict,
                                                            "Categories":theCategoriesList,                                                            
                                                            "MAPS_API_KEY" : 'AIzaSyCJA1o336vHzMhiIAj-3PjLUd2H6xr0be4'},context)


# Reviews
def review(request, *z):
    context = RequestContext(request)
    reviewID = z[0]
    review = Review.objects.get(review_id=reviewID)
    review_votes_list = Review_Votes.objects.filter(review=review)
    return render_to_response('OperationRepo/review.html', {"Review":review, "Review_Votes_List":review_votes_list},context)

# Reviews
def user(request, *z):
    context = RequestContext(request)
    userID = z[0]
    user = User.objects.get(user_id=userID)
    user_votes_list = User_Votes.objects.filter(user=user)
    elite_list = Elite.objects.filter(user=user)
    compliments_list = Compliments.objects.filter(user=user)

    return render_to_response('OperationRepo/user.html', 
        {"User" : user, "User_Votes_List": user_votes_list, 
        "Elite_List":elite_list, "Compliments_List":compliments_list},context)

def business_splash (request):
    context = RequestContext(request)

# Want to get a dictionary with the business name as the key and the business id as the value
    thebusinesses = Business.objects.all()[:10]
    businessIDs = thebusinesses.Business["business_id"]
    #businessNames = thebusinesses.data["name"]
    {"name" : business_id}
    return HttpResponse()
    #return render_to_response('OperationRepo/business_splash.html', {"bdict": thebusinesses},context)

def toJS(a):
    val = str(a.replace("'","\"").replace("True","true").replace("False","false"))
    return json.loads(val)