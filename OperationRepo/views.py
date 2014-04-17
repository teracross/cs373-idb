from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from django.http import StreamingHttpResponse
from django.db.models import Avg
import json
from OperationRepo.forms import SearchForm
from django.db.models import Q
from django.core import serializers



def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {'message': "Hello World", "form": SearchForm(), "active_page" :"index_nav" }
    return render_to_response('OperationRepo/index.html', context_dict, context)


# Businesses
def business(request, *z):
    context = RequestContext(request)
    businessID = z[0]
    thebusiness = get_object_or_404(Business, business_id=str(businessID))
    thereviews = Review.objects.filter(business = thebusiness).order_by('-date').select_related()

    theAttributesList = Attributes.objects.filter(business=thebusiness)
    multiAtrributesDict = {}
    singleAttributesDict = {}
    for objects in theAttributesList :
        if "{" in str(objects.value):
            multiAtrributesDict[objects.name] = toJS(objects.value)
        else :
            singleAttributesDict[objects.name] = objects.value

    theCategoriesList = Categories.objects.filter(business=thebusiness)
    theHoursList = Hours.objects.filter(business=thebusiness)
    
    return render_to_response('OperationRepo/business.html', {"Business" : thebusiness,
                                                            "Reviews":thereviews,
                                                            # "ReviewsArray":thereviews,
                                                            "MultiValueAttributes":multiAtrributesDict,
                                                            "SingleValueAttributes":singleAttributesDict,
                                                            "Categories":theCategoriesList,
                                                            "Hours":theHoursList,
                                                            "MAPS_API_KEY" : 'AIzaSyCJA1o336vHzMhiIAj-3PjLUd2H6xr0be4',
                                                            "form": SearchForm(),
                                                            "active_page" :"business_nav"},context)
# Reviews
def review(request, *z):
    context = RequestContext(request)
    reviewID = z[0]
    review = get_object_or_404(Review, review_id=reviewID)
    review_votes_list = Review_Votes.objects.filter(review=review)
    return render_to_response('OperationRepo/review.html', {"Review":review, "Review_Votes_List":review_votes_list, "form": SearchForm(), "active_page" :"review_nav"},context)

# Reviews
def user(request, *z):
    context = RequestContext(request)
    userID = z[0]
    user = get_object_or_404(User, user_id=userID)
    user_votes_list = User_Votes.objects.filter(user=user)
    elite_list = Elite.objects.filter(user=user).order_by('-years_elite')
    compliments_list = Compliments.objects.filter(user=user)
    users_reviews = Review.objects.filter(user=user).order_by('-date')

    # return HttpResponse([str(i.years_elite) for i in elite_list])
    return render_to_response('OperationRepo/user.html', 
        {"User" : user, "User_Votes_List": user_votes_list, 
        "Elite_List":elite_list, "Compliments_List":compliments_list,
        "reviews":users_reviews,
        "form": SearchForm(),
        "active_page" :"user_nav" },context)

def business_splash (request):
    context = RequestContext(request)
    allBusinesses = Business.objects.all().order_by('name')

    return render_to_response('OperationRepo/business_splash.html', {"bdict": allBusinesses, "form": SearchForm(), "active_page" :"business_nav"},context)

def review_splash (request):
    context = RequestContext(request)
    allReviews = Review.objects.all().order_by("-date")
    avgInfo = allReviews.aggregate(Avg('stars'))
    return render_to_response('OperationRepo/review_splash.html', {"rdict": allReviews, "avgInfo" : avgInfo, "form": SearchForm(), "active_page" :"review_nav"},context)

def user_splash (request):
    context = RequestContext(request)
    allUsers = User.objects.all().order_by('name')

    return render_to_response('OperationRepo/user_splash.html', {"userList": allUsers, "form": SearchForm(), "active_page" :"user_nav"},context)

def search (request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            #form has been submitted
            search = form.cleaned_data['search']
            format = form.cleaned_data['format']
            searchlist = search.split(" ")
            
            qor = Q(text__icontains = str(searchlist[0])) | Q(business__name__icontains = str(searchlist[0])) 
            qor2 = Q(name__icontains = str(searchlist[0]))
            qand = Q(text__icontains = str(searchlist[0])) | Q(business__name__icontains = str(searchlist[0]))
            qand2 = Q(name__icontains = str(searchlist[0]))

            # create qors for queries. or and and 
            for s in searchlist[1:] :
                qor = qor | Q(text__icontains = str(s)) | Q(business__name__icontains = str(s))
                qor2 = qor2 | Q(name__icontains = str(s))
                qand = qand & (Q(text__icontains = str(s)) | Q(business__name__icontains = str(s)))
                qand2 = qand2 & Q(name__icontains = str(s))

            # and search results
            andreviews = Review.objects.filter(qand).select_related()
            andbusinesses = Business.objects.filter(qand2)
            andusers = User.objects.filter(qand2)
            and_results = {"reviews" : andreviews, "businesses" : andbusinesses, "users" : andusers}

            # or search results
            orreviews = Review.objects.filter(qor).exclude(qand).select_related()
            orusers = User.objects.filter(qor2).exclude(qand2)
            orbusinesses = Business.objects.filter(qor2).exclude(qand2)
            or_results = {"reviews" : orreviews, "users" : orusers, "businesses" : orbusinesses}

            form = SearchForm()
            if format == "json":
                context_dict["andresults"] = [serializers.serialize("json", andreviews), serializers.serialize("json", andusers),serializers.serialize("json", andbusinesses)]
                context_dict["orresults"] = [serializers.serialize("json", orreviews), serializers.serialize("json", orusers), serializers.serialize("json", orbusinesses)]
                context_dict["search_terms"] = search
                #context_dict["search_list"] = searchlist
                return StreamingHttpResponse(json.dumps(context_dict))

            context_dict["form"] = form
            context_dict["andresults"] = and_results
            context_dict["orresults"] = or_results 
            context_dict["search_terms"] = search
            context_dict["search_list"] = searchlist

            return render_to_response('OperationRepo/search.html', context_dict, context)
        else:
            form = SearchForm() #create form to display
    return render_to_response('OperationRepo/search.html', {'form':form }, context)


def toJS(a):
    val = str(a.replace("'","\"").replace("True","true").replace("False","false"))
    return json.loads(val)
