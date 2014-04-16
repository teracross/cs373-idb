from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from OperationRepo.models import *
from django.http import HttpResponse
from django.db.models import Avg
from django.db import connections
import json
from OperationRepo.forms import SearchForm



def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {'message': "Hello World", "form": SearchForm(), "active_page" :"index_nav" }

    query = """
    SELECT sub.count as "Number of Compliments",
    ROUND(CAST(SUM(sub.average_stars)/COUNT(*) AS NUMERIC),2) as "Average Stars Given" 
    FROM 
    (
        SELECT u.user_id,COUNT(*),
        u.average_stars 
        FROM "OperationRepo_compliments" c
        join "OperationRepo_user" u on c.user_id=u.user_id
        group by u.user_id
    ) sub
    group by sub.count
    order by "Number of Compliments" """

    q2a = []
    q2b = []
    cursor = connections['default'].cursor()
    cursor.execute(query)
    l = dictfetchall(cursor)

    for g in l :
        a = int(g["Number of Compliments"])
        b = float(g["Average Stars Given"])
        q2a+=[a]
        q2b+=[b]

    query = """
    SELECT COUNT(*), regexp_split_to_table(regexp_replace(lower(text),'[^\sa-zA-Z0-9=+-]','','g'),'\s') as word
    from "OperationRepo_review" as r
    group by word
    order by count desc
    limit 10;"""

    q3a = []
    q3b = []
    cursor = connections['default'].cursor()
    cursor.execute(query)
    l = dictfetchall(cursor)

    for g in l :
        a = str(g["word"])
        b = int(g["count"])
        q3a+=[a]
        q3b+=[b]        

    return render_to_response('OperationRepo/index.html', {"q2a":q2a,"q2b":q2b, "q3a":q3a,"q3b":q3b, "form": SearchForm(), "active_page" :"index_nav" }, context)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

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

    reviewHistoryLabels = []
    reviewHistoryVolumeData = []
    reviewHistoryStarsData = []
    cursor = connections['default'].cursor()

    query = """SELECT date_part('month',date) as month ,date_part('year',date) as year,
    count(*) as count, AVG(stars) as avg FROM "OperationRepo_review" where business_id='"""+businessID+"""'
    group by year,month order by year,month"""
    cursor.execute(query)

    l = dictfetchall(cursor)
    for g in l :
        label = str(int(g["month"]))+"/"+str(int(g["year"]))
        reviewHistoryLabels+=[label]
        reviewHistoryVolumeData+=[int(g["count"])]
        reviewHistoryStarsData+=[g["avg"]]

    return render_to_response('OperationRepo/business.html', {"Business" : thebusiness,
                                                            "Reviews":thereviews,
                                                            # "ReviewsArray":thereviews,
                                                            "MultiValueAttributes":multiAtrributesDict,
                                                            "SingleValueAttributes":singleAttributesDict,
                                                            "Categories":theCategoriesList,
                                                            "Hours":theHoursList,
                                                            "MAPS_API_KEY" : 'AIzaSyCJA1o336vHzMhiIAj-3PjLUd2H6xr0be4',
                                                            "form": SearchForm(),
                                                            "reviewHistoryLabels" : reviewHistoryLabels,
                                                            "reviewHistoryVolumeData" : reviewHistoryVolumeData,
                                                            "reviewHistoryStarsData" : reviewHistoryStarsData,
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
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            #form has been submitted
            search = form.cleaned_data['search']
            search_results = []
            reviews = Review.objects.filter(text__contains = str(search))
            businesses = Business.objects.filter(name__contains = str(search))
            users = User.objects.filter(name__contains = str(search))
            search_results = [reviews, businesses, users]
            form = SearchForm()
            return render_to_response('OperationRepo/search.html', {"results" : search_results, "form" : form, "search_terms": str(search)}, context)
        else:
            form = SearchForm() #create form to display
    return render_to_response('OperationRepo/search.html', {"results": [], 'form':form}, context)


def toJS(a):
    val = str(a.replace("'","\"").replace("True","true").replace("False","false"))
    return json.loads(val)
