from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db import connections

from OperationRepo import models
from django.http import HttpResponse
import json
import ast

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'message': "Hello World"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('OperationRepo/index.html', context_dict, context)
def sortHours(businessDictionary):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    sortedHours = []
    for day in days :
        hoursDict = businessDictionary["hours"]
        if day in hoursDict :
            thed = {"day" : day, "open" : hoursDict[day]["open"], "close" : hoursDict[day]["close"]}
            sortedHours.append(thed)
    businessDictionary["hours"] = sortedHours
    return businessDictionary
def truncateName(n) :
    return n[:10]+"..."

def getJsonOneRow(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    for row in cursor.fetchall() :
        return str(row)

def getJsonColumns(cursor, l) :
     for row in cursor.fetchall() :
        d = {}
        for index in l :
            d.update(row[index])
        return str(d)

# Businesses
def business(request, *z):
    context = RequestContext(request)
    businessID = int(z[0])
    cursor = connections['default'].cursor()
    cursor.execute("SELECT data from businesses where pkbusinessid="+str(businessID));

    s1 = getJsonOneRow(cursor)
    s1 = s1.replace("'","\"")
    s1 = s1.replace("True","true")
    s1 = s1.replace("False","false")
    s1 = s1.replace("(","")
    s1 = s1.replace(",)","")
    j = json.loads(s1)
    json_type = j.pop("type", None)
    #j.pop("hours", None)
    #j.pop("attributes", None)
    #hours = models.Hours(json.loads(j.pop("hours", None)))
    #attributes = models.Attributes(json.loads(j.pop("attributes", None)))
    is_open = j.pop("open", None)
    #hours = json.load(hours)
    business = models.Business(**j)

    business.is_open = is_open
    business.json_type = json_type
    #return HttpResponse(business.business_id)
    #return render_to_response('OperationRepo/business.html', d, context)
    #context_dict = sortHours(context_dict)
    return render_to_response('OperationRepo/business.html', {"business" : business, "a" : businessID, "json" : j},context)


# Reviews
def review(request, *z):
    context = RequestContext(request)
    reviewID = z[0]
    cursor = connections['default'].cursor()
    cursor.execute("SELECT reviews.data, users.data->>'name' from reviews join users on users.data->>\'user_id\'=reviews.data->>\'user_id\' where reviews.data->>\'review_id\'=\'"+str(reviewID)+"\'")
    d = {}
    for row in cursor.fetchall() :
        d = row[0]
        username = row[1]
        d["username"] = username
        break
    r1 = str(d)
    r1 = r1.replace("True","true")
    r1 = r1.replace("False","false")
    r1 = r1.replace("(","") 
    r1 = r1.replace(",)","")    
    j = ast.literal_eval(r1)
    j.pop("votes",None)
    j.pop("type",None)
    thereview = models.Review(**j)
    return render_to_response('OperationRepo/review.html', {"review" : thereview},context)
    
    #review = models.Review(**j)
    #return render_to_response('OperationRepo/review.html', {"review" : review}, context)


# Users
def user(request, *z):
    context = RequestContext(request)
    a = int(z[0])
    if a == 1 :
        context_dict = {"a" : a , "yelping_since": "2008-05", "votes": {"funny": 535, "useful": 975, "cool": 503}, "review_count": 425, "name": "Fred", "user_id": "JgDkCER12uiv4lbpmkZ9VA", "friends": ["A_O8wZOsMTPwyeYA4-Rsow", "y4JCKsEm0KlwtmHpZhbA4A", "AkLRwgw9ljUqXWyBNzpqXQ", "qASPib1Z8ft8e96dtbh66w", "tlSSQwfHYJany7wPoTH46A", "lPaYMDmJbAnv_3pmZH_inw", "3nZmdlyJ-11H1ImZ_HKbmw", "P2kVk4cIWyK4e4h14RhK-Q", "ioTuTA_pI-ZgiM4uISDQPg", "fczQCSmaWF78toLEmb0Zsw", "q9XgOylNsSbqZqF_SO3-OQ", "HZeFzs42f0iGaA-sP_hUnA", "MUHoBFzwRoXpCpgYSN8KRA", "0qIsBt4EzBDCKrIviV55Ew", "-F32Vl8Rk4dwsmk0f2wRIw", "uVU1FyUPPVxzZ8jbye-rFA", "-txH2zJSBZQHO6RWvoWXuQ", "C6IOtaaYdLIT5fWd7ZYIuA", "sEWeeq41k4ohBz4jS_iGRw", "MwJVSTsUB-htphNZaIC43g", "GubdNFoDAsiwE6bWIr97cQ", "UsULgP4bKA8RMzs8dQzcsA", "rjlb-7-JcmM6fR64ZpyTug", "vyFYFsQMkHkN3vw5jPuCZw", "4j8c0ttT0OcIYTrARYQZNQ", "tdNV2Wb0LrFpm1Yfov_Klw", "qwu5B9anH4AlEtau0K-6aQ", "r-t7IiTSD0QZdt8lOUCqeQ", "fkZ_t7co7VxO2jPI9bD5bg", "o1HQEND6cg-4SK0Z1ASBMQ", "y9IKf7VckFc-fesWuDwgxg", "V1F7D9udQkOXykFPvbBKmQ", "z1c8uQv7tfgrP4-sVggbTA", "ZZ43etAB2n_T53YBYtf8Dw", "3f_-pGlAZi6a6ZySrsspVQ", "VD101SO18FEaE0vM7x4iEQ", "vsXP832M0kOxKpfduD7dWw", "9y7Ni5EInmU20ySEs8ymyw", "HaDEZSNSTNFmq6laVB6ZMQ", "E5QyEU6FCQwnTys0S73zNw", "JkMOQaMjlBHMqp6gj-hL3w", "MWt24-6bfv_OHLKhwMQ0Tw", "_wY1dHBXKN4NjB5IsIk4eQ", "l81ILmOhky5bG7o4r3rkhQ", "t79B56n8IeVrMNmM4QU2Ow", "Q96IRvil6RNgdLmGKuh81A", "OqisxqKDGaZwEvLm1OG4dg", "zCC6huLkNBEr3JUgQyxJbg", "5B5fyTX11NXiaf9HGeLCXQ", "fev0iI-XDrteD4SYRKjiUw", "uZetl9T0NcROGOyFfughhg", "mQba83gB018LlGt51r80ZQ", "IO3AsR6cdMto7VCwfPzf2w", "6qTA7oelKwpevf1lL_bIVA", "GnZWh25MyJD1d5FMKl3QmA", "hjJPKQ1Ah91h3fVbc8GsOg", "GrSixRnGIxNUJ1Cn5DNX9A", "oy6fdscGSXY2gzRqF9pZxg", "WWxCMDn8rVHIrIFoKRcRDg", "0VfJi9Au0rVFVnPKcJpt3Q", "UK1Be04VKd1k2JnScw-_bw", "usQTOj7LQ9v0Fl98gRa3Iw", "--65q1FpAL_UQtVZ2PTGew", "MTu3hVSZkK8nkPhqT2FIDQ", "L3XWX_dd8_pYnRSMdppjDg", "eeEj90eJiwYMLJfPW9kdxg", "yyVaDXsgGPw3vl2bv-1R3w", "eBwBjylS66qPcHs2_ajLag", "WsJo2lfomyGzgIFmVtFgiw", "G8YrBFZS2Kb5LQCap-br_g", "xZvRLPJ1ixhFVomkXSfXAw", "4ozupHULqGyO42s3zNUzOQ", "QdypppSRw2H5UtMu1IebLw", "U7oMbMxoF0T-RlU4PhZGAA", "pv82zTlB5Txsu2Pusu__FA", "BLUDPZW_d2fAF0Pia28ZlA", "d95On_QNeQPr01pRNzHa5w", "qzND3A_Nv89M4sQn8B4TXg", "33vUIil_GCaT92aUaZhRXA", "-OMlS6yWkYjVldNhC31wYg", "Ux7a5tbceLU6anNycjwt_Q", "vn3lecMsL3kXVe-7hg3gLg", "zZxr7X10CDThXZbnkLmNVA", "R86wR3cHNJDPea5uGAGsGw", "YPwFl3RCRwr-kyN-890STA", "X_kPh3nt0AJPNPHye2rTlA", "9ZbwFZhqWVwdbuYSP_FjWg", "fXNWwZM96eNVpShklrOdhA", "XpSZrY_Ym8GGx7SNEd0q9g"], "fans": 10, "average_stars": 3.4399999999999999, "type": "user", "compliments": {"profile": 2, "funny": 18, "plain": 41, "writer": 12, "list": 4, "note": 36, "photos": 1, "hot": 25, "cool": 22, "more": 1}, "elite": [2008], "json" : """{
    "yelping_since": "2008-05",
    "votes": {
        "funny": 535,
        "useful": 975,
        "cool": 503
    },
    "review_count": 425,
    "name": "Fred",
    "user_id": "JgDkCER12uiv4lbpmkZ9VA",
    "friends": [
        "A_O8wZOsMTPwyeYA4-Rsow",
        "y4JCKsEm0KlwtmHpZhbA4A",
        "AkLRwgw9ljUqXWyBNzpqXQ",
        "qASPib1Z8ft8e96dtbh66w",
        "tlSSQwfHYJany7wPoTH46A",
        "lPaYMDmJbAnv_3pmZH_inw",
        "3nZmdlyJ-11H1ImZ_HKbmw",
        "P2kVk4cIWyK4e4h14RhK-Q",
        "ioTuTA_pI-ZgiM4uISDQPg",
        "fczQCSmaWF78toLEmb0Zsw",
        "q9XgOylNsSbqZqF_SO3-OQ",
        "HZeFzs42f0iGaA-sP_hUnA",
        "MUHoBFzwRoXpCpgYSN8KRA",
        "0qIsBt4EzBDCKrIviV55Ew",
        "-F32Vl8Rk4dwsmk0f2wRIw",
        "uVU1FyUPPVxzZ8jbye-rFA",
        "-txH2zJSBZQHO6RWvoWXuQ",
        "C6IOtaaYdLIT5fWd7ZYIuA",
        "sEWeeq41k4ohBz4jS_iGRw",
        "MwJVSTsUB-htphNZaIC43g",
        "GubdNFoDAsiwE6bWIr97cQ",
        "UsULgP4bKA8RMzs8dQzcsA",
        "rjlb-7-JcmM6fR64ZpyTug",
        "vyFYFsQMkHkN3vw5jPuCZw",
        "4j8c0ttT0OcIYTrARYQZNQ",
        "tdNV2Wb0LrFpm1Yfov_Klw",
        "qwu5B9anH4AlEtau0K-6aQ",
        "r-t7IiTSD0QZdt8lOUCqeQ",
        "fkZ_t7co7VxO2jPI9bD5bg",
        "o1HQEND6cg-4SK0Z1ASBMQ",
        "y9IKf7VckFc-fesWuDwgxg",
        "V1F7D9udQkOXykFPvbBKmQ",
        "z1c8uQv7tfgrP4-sVggbTA",
        "ZZ43etAB2n_T53YBYtf8Dw",
        "3f_-pGlAZi6a6ZySrsspVQ",
        "VD101SO18FEaE0vM7x4iEQ",
        "vsXP832M0kOxKpfduD7dWw",
        "9y7Ni5EInmU20ySEs8ymyw",
        "HaDEZSNSTNFmq6laVB6ZMQ",
        "E5QyEU6FCQwnTys0S73zNw",
        "JkMOQaMjlBHMqp6gj-hL3w",
        "MWt24-6bfv_OHLKhwMQ0Tw",
        "_wY1dHBXKN4NjB5IsIk4eQ",
        "l81ILmOhky5bG7o4r3rkhQ",
        "t79B56n8IeVrMNmM4QU2Ow",
        "Q96IRvil6RNgdLmGKuh81A",
        "OqisxqKDGaZwEvLm1OG4dg",
        "zCC6huLkNBEr3JUgQyxJbg",
        "5B5fyTX11NXiaf9HGeLCXQ",
        "fev0iI-XDrteD4SYRKjiUw",
        "uZetl9T0NcROGOyFfughhg",
        "mQba83gB018LlGt51r80ZQ",
        "IO3AsR6cdMto7VCwfPzf2w",
        "6qTA7oelKwpevf1lL_bIVA",
        "GnZWh25MyJD1d5FMKl3QmA",
        "hjJPKQ1Ah91h3fVbc8GsOg",
        "GrSixRnGIxNUJ1Cn5DNX9A",
        "oy6fdscGSXY2gzRqF9pZxg",
        "WWxCMDn8rVHIrIFoKRcRDg",
        "0VfJi9Au0rVFVnPKcJpt3Q",
        "UK1Be04VKd1k2JnScw-_bw",
        "usQTOj7LQ9v0Fl98gRa3Iw",
        "--65q1FpAL_UQtVZ2PTGew",
        "MTu3hVSZkK8nkPhqT2FIDQ",
        "L3XWX_dd8_pYnRSMdppjDg",
        "eeEj90eJiwYMLJfPW9kdxg",
        "yyVaDXsgGPw3vl2bv-1R3w",
        "eBwBjylS66qPcHs2_ajLag",
        "WsJo2lfomyGzgIFmVtFgiw",
        "G8YrBFZS2Kb5LQCap-br_g",
        "xZvRLPJ1ixhFVomkXSfXAw",
        "4ozupHULqGyO42s3zNUzOQ",
        "QdypppSRw2H5UtMu1IebLw",
        "U7oMbMxoF0T-RlU4PhZGAA",
        "pv82zTlB5Txsu2Pusu__FA",
        "BLUDPZW_d2fAF0Pia28ZlA",
        "d95On_QNeQPr01pRNzHa5w",
        "qzND3A_Nv89M4sQn8B4TXg",
        "33vUIil_GCaT92aUaZhRXA",
        "-OMlS6yWkYjVldNhC31wYg",
        "Ux7a5tbceLU6anNycjwt_Q",
        "vn3lecMsL3kXVe-7hg3gLg",
        "zZxr7X10CDThXZbnkLmNVA",
        "R86wR3cHNJDPea5uGAGsGw",
        "YPwFl3RCRwr-kyN-890STA",
        "X_kPh3nt0AJPNPHye2rTlA",
        "9ZbwFZhqWVwdbuYSP_FjWg",
        "fXNWwZM96eNVpShklrOdhA",
        "XpSZrY_Ym8GGx7SNEd0q9g"
    ],
    "fans": 10,
    "average_stars": 3.44,
    "type": "user",
    "compliments": {
        "profile": 2,
        "funny": 18,
        "plain": 41,
        "writer": 12,
        "list": 4,
        "note": 36,
        "photos": 1,
        "hot": 25,
        "cool": 22,
        "more": 1
    },
    "elite": [
        2008
    ]
}"""}
    elif a == 2 :
        context_dict = {"a" : a , "yelping_since": "2010-05", "votes": {"funny": 0, "useful": 4, "cool": 0}, "review_count": 1, "name": "Christi", "user_id": "SS85hfTApRnbTPcJadra8A", "friends": [], "fans": 0, "average_stars": 5.0, "type": "user", "compliments": {}, "elite": [], "json" : """{
    "yelping_since": "2010-05",
    "votes": {
        "funny": 0,
        "useful": 4,
        "cool": 0
    },
    "review_count": 1,
    "name": "Christi",
    "user_id": "SS85hfTApRnbTPcJadra8A",
    "friends": [],
    "fans": 0,
    "average_stars": 5,
    "type": "user",
    "compliments": {},
    "elite": []
}"""}
    else :
        context_dict = {"a" : a , "yelping_since": "2011-07", "votes": {"funny": 64, "useful": 442, "cool": 166}, "review_count": 381, "name": "Melissa", "user_id": "fR6Vch-D0L6OBnLMl8f9Sg", "friends": ["fczQCSmaWF78toLEmb0Zsw", "uBp2Jmip2qXQ0iWHUDY9sQ", "KM9I3k5D7aCtqBG5DiqHeA", "IyxFBaOOAMke-ER4RVhuqQ", "Za9CEz4x9Ks-94W0lqvuPg", "5_2BuK-IWiuLhZ9VGBRYYw", "2_tOvm9THqfuxiXSxbE7Zw", "rSbqoimVUWPEbNSGwyjI-Q", "lC0KGXmIhyjzghBUlVnkhQ", "4ISIH0HF6h2FuRm41s_NzQ", "rF7PJO_wur7GMr7rIR7ntw", "WnKrxD7P4CQGXyOrMyLIjw", "J2JfCaiaZku8HgfNceU8Rg", "cRyNICH0mhjxagvSyVr60Q", "23-FXvM7P1ZJFawV3ccZ1Q", "LTc0zVEC1mOwsxeZTMer0A", "AbO18pf8bXG1qF9bb9L6wQ", "-Nfj9wmdsm0cbH6aIJHKsQ", "xAVu2pZ6nIvkdHh8vGs84Q", "HnqzojvN3AyZHjslUlxiJQ", "v6rb-4YhADpuD99f3RKmgg", "gQMuqiadl4WXnB58fljphw", "_YtM7pgpvrEWUJdpY-_S-A", "HestW1GKSkmUs_vpnauE_w"], "fans": 8, "average_stars": 4.1600000000000001, "type": "user", "compliments": {"profile": 1, "funny": 1, "plain": 11, "writer": 10, "note": 9, "photos": 1, "hot": 11, "cool": 9, "more": 5}, "elite": [], "json" : """{
    "yelping_since": "2011-07",
    "votes": {
        "funny": 64,
        "useful": 442,
        "cool": 166
    },
    "review_count": 381,
    "name": "Melissa",
    "user_id": "fR6Vch-D0L6OBnLMl8f9Sg",
    "friends": [
        "fczQCSmaWF78toLEmb0Zsw",
        "uBp2Jmip2qXQ0iWHUDY9sQ",
        "KM9I3k5D7aCtqBG5DiqHeA",
        "IyxFBaOOAMke-ER4RVhuqQ",
        "Za9CEz4x9Ks-94W0lqvuPg",
        "5_2BuK-IWiuLhZ9VGBRYYw",
        "2_tOvm9THqfuxiXSxbE7Zw",
        "rSbqoimVUWPEbNSGwyjI-Q",
        "lC0KGXmIhyjzghBUlVnkhQ",
        "4ISIH0HF6h2FuRm41s_NzQ",
        "rF7PJO_wur7GMr7rIR7ntw",
        "WnKrxD7P4CQGXyOrMyLIjw",
        "J2JfCaiaZku8HgfNceU8Rg",
        "cRyNICH0mhjxagvSyVr60Q",
        "23-FXvM7P1ZJFawV3ccZ1Q",
        "LTc0zVEC1mOwsxeZTMer0A",
        "AbO18pf8bXG1qF9bb9L6wQ",
        "-Nfj9wmdsm0cbH6aIJHKsQ",
        "xAVu2pZ6nIvkdHh8vGs84Q",
        "HnqzojvN3AyZHjslUlxiJQ",
        "v6rb-4YhADpuD99f3RKmgg",
        "gQMuqiadl4WXnB58fljphw",
        "_YtM7pgpvrEWUJdpY-_S-A",
        "HestW1GKSkmUs_vpnauE_w"
    ],
    "fans": 8,
    "average_stars": 4.16,
    "type": "user",
    "compliments": {
        "profile": 1,
        "funny": 1,
        "plain": 11,
        "writer": 10,
        "note": 9,
        "photos": 1,
        "hot": 11,
        "cool": 9,
        "more": 5
    },
    "elite": []
}"""}
    return render_to_response('OperationRepo/user.html', context_dict, context)