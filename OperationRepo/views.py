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
            multiAtrributesDict[objects.name] = objects.value
        else :
            singleAttributesDict[objects.name] = objects.value


    # theAttributesList = Attributes.objects.filter(business=thebusiness).exclude(name="Good For").exclude(name="Parking")
    # goodFor = toJS(Attributes.objects.filter(name="Good For", business=thebusiness))
    # parking = toJS(Attributes.objects.filter(name="Parking", business=thebusiness))


    return render_to_response('OperationRepo/business.html', {"Business" : thebusiness,
                                                            "Reviews":thereviews,
                                                            # "ReviewsArray":thereviews,
                                                            "MultiValueAttributes":multiAtrributesDict,
                                                            "SingleValueAttributes":singleAttributesDict,
                                                            "MAPS_API_KEY" : 'AIzaSyCJA1o336vHzMhiIAj-3PjLUd2H6xr0be4'},context)


# Reviews
def review(request, *z):
    context = RequestContext(request)
    reviewID = z[0]
    thereview = Review.objects.get(review_id=str(reviewID))
    theuser = User.objects.get(data__contains="\"user_id\": \""+thereview.data["user_id"])
    thebusiness = Business.objects.get(data__contains=str(thereview.data["business_id"]))
    thebusiness.data["name"] = thebusiness.data["name"][0:12]+"..."
    return render_to_response('OperationRepo/review.html', {"Review" : thereview,"User":theuser,"Business":thebusiness,"json":str(thereview.data)},context)

# Reviews
def user(request, *z):
    context = RequestContext(request)
    userID = z[0]
    theuser = User.objects.get(user_id="\"user_id\": \""+userID)
    friendsArray = str(theuser.data["friends"]).replace("u'","\"").replace("'","\"")
    return render_to_response('OperationRepo/user.html', {"User" : theuser,"json":str(theuser.data),"FriendsArray":friendsArray},context)


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
    val = str(a[0].value.replace("'","\"").replace("True","true").replace("False","false"))
    return json.loads(val)

# def toJSArray(l,c) :
#     s = "["
#     for obj in l :
#         s+="{"
#         for col in c :
#             s+=col+":"+"'"+str(obj.data[col])+"',"
#         s = s[:-1]
#         s+="},"
#     s = s[:-1]
#     s+="]"
#     return s
