from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from OperationRepo.models import Review
from OperationRepo.models import User
from OperationRepo.models import Business
from django.http import HttpResponse

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
    thebusiness = Business.objects.get(data__contains=str(businessID))
    thereviews = Review.objects.filter(data__contains=str(thebusiness.data["business_id"]))
    reviewsArray = toJSArray(thereviews,["stars","review_id"])
    goodFor = thebusiness.data["attributes"].pop("Good For")
    parking = thebusiness.data["attributes"].pop("Parking")
    theAttributesList = thebusiness.data["attributes"].items()
    return render_to_response('OperationRepo/business.html', {"Business" : thebusiness,"json":str(thebusiness.data),
                                                              "Reviews":thereviews,"ReviewsArray":str(reviewsArray),"AttributesList":theAttributesList,
                                                              "GoodFor":goodFor,"Parking":parking},context)


# Reviews
def review(request, *z):
    context = RequestContext(request)
    reviewID = z[0]
    thereview = Review.objects.get(data__contains=str(reviewID))
    theuser = User.objects.get(data__contains="\"user_id\": \""+thereview.data["user_id"])
    thebusiness = Business.objects.get(data__contains=str(thereview.data["business_id"]))
    thebusiness.data["name"] = thebusiness.data["name"][0:12]+"..."
    return render_to_response('OperationRepo/review.html', {"Review" : thereview,"User":theuser,"Business":thebusiness,"json":str(thereview.data)},context)

# Reviews
def user(request, *z):
    context = RequestContext(request)
    userID = z[0]
    theuser = User.objects.get(data__contains="\"user_id\": \""+userID)
    return render_to_response('OperationRepo/user.html', {"User" : theuser,"json":str(theuser.data)},context)

def toJSArray(l,c) :
    s = "["
    for obj in l :
        s+="{"
        for col in c :
            s+=col+":"+"'"+str(obj.data[col])+"',"
        s = s[:-1]
        s+="},"
    s = s[:-1]
    s+="]"
    return s