from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

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
# Businesses
def business(request, *z):
    context = RequestContext(request)
    a = int(z[0])
    if a == 1 :
        context_dict = {"a" : a , "business_id": "WIcDFpHEnC3ihNmS7-6-ZA", "full_address": "7605 E Pinnacle Peak Rd\nScottsdale, AZ 85255", "hours": {"Monday": {"close": "20:30", "open": "11:00"}, "Tuesday": {"close": "20:30", "open": "11:00"}, "Friday": {"close": "21:00", "open": "11:00"}, "Wednesday": {"close": "20:30", "open": "11:00"}, "Thursday": {"close": "20:30", "open": "11:00"}, "Saturday": {"close": "21:00", "open": "17:00"}} , "close": "21:00", "open": "17:00", "open": False, "categories": "Thai,Restaurants", "city": "Scottsdale", "review_count": 21, "name": "Thai Pan Fresh Exotic Cuisine", "longitude": -111.9174872, "state": "AZ", "stars": 3.5, "latitude": 33.698649699999997, "attributes": {"Take-out": True,  "Takes Reservations": False, "Delivery": False, "Wheelchair Accessible": True, "Outdoor Seating": False, "Attire": "casual", "Alcohol": "beer_and_wine", "Waiter Service": False, "Accepts Credit Cards": True, "Good for Kids": True, "Good For Groups": True, "Price Range": 2}, "goodfor": {"dessert": False, "latenight": False, "lunch": True, "dinner": True, "brunch": False, "breakfast": False}, "Parking": {"garage": False, "street": False, "validated": False, "lot": True, "valet": False}, "type": "business", "yelpurl" : "http://www.yelp.com/biz/thai-pan-fresh-exotic-cuisine-scottsdale", "json" : """{
    "business_id": "WIcDFpHEnC3ihNmS7-6-ZA",
    "full_address": "7605 E Pinnacle Peak Rd\nScottsdale, AZ 85255",
    "hours": {
        "Monday": {
            "close": "20:30",
            "open": "11:00"
        },
        "Tuesday": {
            "close": "20:30",
            "open": "11:00"
        },
        "Friday": {
            "close": "21:00",
            "open": "11:00"
        },
        "Wednesday": {
            "close": "20:30",
            "open": "11:00"
        },
        "Thursday": {
            "close": "20:30",
            "open": "11:00"
        },
        "Saturday": {
            "close": "21:00",
            "open": "17:00"
        }
    },
    "open": false,
    "categories": [
        "Thai",
        "Restaurants"
    ],
    "city": "Scottsdale",
    "review_count": 21,
    "name": "Thai Pan Fresh Exotic Cuisine",
    "neighborhoods": [],
    "longitude": -111.9174872,
    "state": "AZ",
    "stars": 3.5,
    "latitude": 33.6986497,
    "attributes": {
        "Take-out": true,
        "Good For": {
            "dessert": false,
            "latenight": false,
            "lunch": true,
            "dinner": true,
            "brunch": false,
            "breakfast": false
        },
        "Takes Reservations": false,
        "Delivery": false,
        "Parking": {
            "garage": false,
            "street": false,
            "validated": false,
            "lot": true,
            "valet": false
        },
        "Wheelchair Accessible": true,
        "Outdoor Seating": false,
        "Attire": "casual",
        "Alcohol": "beer_and_wine",
        "Waiter Service": false,
        "Accepts Credit Cards": true,
        "Good for Kids": true,
        "Good For Groups": true,
        "Price Range": 2
    },
    "type": "business"
}"""}
        context_dict = sortHours(context_dict)
    elif a == 2 :
        context_dict = {"a" : a , "business_id": "70p94Ejeu1v5XlIkbKORYQ", "full_address": "3479 E Baseline Rd\nSte 18\nGilbert, AZ 85234", "hours": {"Monday": {"close": "19:00", "open": "09:00"}, "Tuesday": {"close": "19:00", "open": "09:00"}, "Friday": {"close": "19:00", "open": "09:00"}, "Wednesday": {"close": "19:00", "open": "09:00"}, "Thursday": {"close": "19:00", "open": "09:00"}, "Saturday": {"close": "19:00", "open": "09:00"}} , "open": "True", "categories": "Hair Salons,Beauty & Spas", "city": "Gilbert", "review_count": 9, "name": "Salon Lola", "longitude": -111.75560249999999, "state": "AZ", "stars": 5.0, "latitude": 33.379065699999998, "attributes": {"Price Range": 2, "By Appointment Only": "True", "Accepts Credit Cards": "True", "Good for Kids": "True", "Wheelchair Accessible": "True"}, "Parking": {"garage": "False", "street": "False", "validated": "False", "lot": "True", "valet": "False"}, "type": "business", "yelpurl" : "http://www.yelp.com/biz/salon-lola-gilbert", "json" : """{
    "business_id": "70p94Ejeu1v5XlIkbKORYQ",
    "full_address": "3479 E Baseline Rd\nSte 18\nGilbert, AZ 85234",
    "hours": {
        "Monday": {
            "close": "19:00",
            "open": "09:00"
        },
        "Tuesday": {
            "close": "19:00",
            "open": "09:00"
        },
        "Friday": {
            "close": "19:00",
            "open": "09:00"
        },
        "Wednesday": {
            "close": "19:00",
            "open": "09:00"
        },
        "Thursday": {
            "close": "19:00",
            "open": "09:00"
        },
        "Saturday": {
            "close": "19:00",
            "open": "09:00"
        }
    },
    "open": true,
    "categories": [
        "Hair Salons",
        "Beauty & Spas"
    ],
    "city": "Gilbert",
    "review_count": 9,
    "name": "Salon Lola",
    "neighborhoods": [],
    "longitude": -111.7556025,
    "state": "AZ",
    "stars": 5,
    "latitude": 33.3790657,
    "attributes": {
        "Price Range": 2,
        "Parking": {
            "garage": false,
            "street": false,
            "validated": false,
            "lot": true,
            "valet": false
        },
        "By Appointment Only": true,
        "Accepts Credit Cards": true,
        "Good for Kids": true,
        "Wheelchair Accessible": true
    },
    "type": "business"
}"""}
    else :
        context_dict = {"a" : a , "business_id": "WcGTSRku3mrVK7V9GKq4UQ", "full_address": "1084 S Gilbert Rd\nGilbert, AZ 85296", "hours": {}, "open": "True", "categories": "Fast Food,Tex-Mex,Restaurants", "city": "Gilbert", "review_count": 31, "name": "Chipotle Mexican Grill", "longitude": -111.790869, "state": "AZ", "stars": 4.0, "latitude": 33.329841999999999, "attributes": {"Take-out": "True", "Noise Level": "average", "Good for Kids": "True", "Takes Reservations": "False", "Has TV": "False", "BYOB/Corkage": "yes_free", "Delivery": "False", "Ambience": {"romantic": "False", "intimate": "False", "touristy": "False", "hipster": "False", "divey": "False", "classy": "False", "trendy": "False", "upscale": "False", "casual": "False"},"Wheelchair Accessible": "True", "Corkage": "False", "Outdoor Seating": "True", "Attire": "casual", "Alcohol": "none", "Waiter Service": "False", "Accepts Credit Cards": "True", "Good For Kids": "True", "Good For Groups": "False", "Price Range": 1}, "goodfor": {"dessert": "False", "latenight": "False", "lunch": "True", "dinner": "True", "brunch": "False", "breakfast": "False"},  "Parking": {"garage": "False", "street": "False", "validated": "False", "lot": "True", "valet": "False"}, "type": "business", "yelpurl" : "http://www.yelp.com/biz/chipotle-mexican-grill-gilbert-2", "json" : """{
    "business_id": "WcGTSRku3mrVK7V9GKq4UQ",
    "full_address": "1084 S Gilbert Rd\nGilbert, AZ 85296",
    "hours": {},
    "open": true,
    "categories": [
        "Fast Food",
        "Tex-Mex",
        "Restaurants"
    ],
    "city": "Gilbert",
    "review_count": 31,
    "name": "Chipotle Mexican Grill",
    "neighborhoods": [],
    "longitude": -111.790869,
    "state": "AZ",
    "stars": 4,
    "latitude": 33.329842,
    "attributes": {
        "Take-out": true,
        "Good For": {
            "dessert": false,
            "latenight": false,
            "lunch": true,
            "dinner": true,
            "brunch": false,
            "breakfast": false
        },
        "Noise Level": "average",
        "Good for Kids": true,
        "Takes Reservations": false,
        "Has TV": false,
        "BYOB/Corkage": "yes_free",
        "Delivery": false,
        "Ambience": {
            "romantic": false,
            "intimate": false,
            "touristy": false,
            "hipster": false,
            "divey": false,
            "classy": false,
            "trendy": false,
            "upscale": false,
            "casual": false
        },
        "Parking": {
            "garage": false,
            "street": false,
            "validated": false,
            "lot": true,
            "valet": false
        },
        "Wheelchair Accessible": true,
        "Corkage": false,
        "Outdoor Seating": true,
        "Attire": "casual",
        "Alcohol": "none",
        "Waiter Service": false,
        "Accepts Credit Cards": true,
        "Good For Kids": true,
        "Good For Groups": false,
        "Price Range": 1
    },
    "type": "business"
}"""}
    return render_to_response('OperationRepo/business.html', context_dict, context)

# Reviews
def review(request, *z):
    context = RequestContext(request)
    a = int(z[0])
    if a == 1 :
        context_dict = {"a" : a , "user": "Fred", "name": "Thai Pan Fresh Exotic Cuisine", "votes": {"funny": 1, "useful": 1, "cool": 1}, "user_id": "r-t7IiTSD0QZdt8lOUCqeQ", "review_id": "0ESSqLfOae77muWTv_zUqA", "stars": 3, "date": "2011-02-11", "text": "Lately i have been feeling homesick for asian food and been hitting up places that i haven't been to in awhile.  Recently re-visited Thai Pan for a quick lunch and quickly ordered without spending too much time perusing the menu.  It looked more diverse than I remembered including some Vietnamese additions.  I remembered the curries and stir-fry dishes were ok but nothing really memorable.  A quick summary for my latest visit:\n\nPros:\n- convenient order-at-the counter setup\n- self-serve drink station\n- brown and white rice mixture\n- friendly and gracious owners\n\nCons:\n- too much napa cabbage in comparison to green vegetables \n- wish the owner/chef would be back in the kitchen vs. managing\n- spice level on the weak side", "type": "review", "business_id": "WIcDFpHEnC3ihNmS7-6-ZA","json" : """{
    "votes": {
        "funny": 1,
        "useful": 1,
        "cool": 1
    },
    "user_id": "r-t7IiTSD0QZdt8lOUCqeQ",
    "review_id": "0ESSqLfOae77muWTv_zUqA",
    "stars": 3,
    "date": "2011-02-11",
    "text": "Lately i have been feeling homesick for asian food and been hitting up places that i haven't been to in awhile.  Recently re-visited Thai Pan for a quick lunch and quickly ordered without spending too much time perusing the menu.  It looked more diverse than I remembered including some Vietnamese additions.  I remembered the curries and stir-fry dishes were ok but nothing really memorable.  A quick summary for my latest visit:\n\nPros:\n- convenient order-at-the counter setup\n- self-serve drink station\n- brown and white rice mixture\n- friendly and gracious owners\n\nCons:\n- too much napa cabbage in comparison to green vegetables \n- wish the owner/chef would be back in the kitchen vs. managing\n- spice level on the weak side",
    "type": "review",
    "business_id": "WIcDFpHEnC3ihNmS7-6-ZA"
}"""}
        context_dict["shortname"] = truncateName(context_dict["name"])
    elif a == 2 :
        context_dict = {"a" : a , "user": "Christi", "name": "Salon Lola", "votes": {"funny": 0, "useful": 0, "cool": 0}, "user_id": "SS85hfTApRnbTPcJadra8A", "review_id": "VyAKIaj_Rmsf_ZCHcGJyUw", "stars": 5, "date": "2010-05-30", "text": "I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.", "type": "review", "business_id": "70p94Ejeu1v5XlIkbKORYQ", "json" : """{
    "votes": {
        "funny": 0,
        "useful": 0,
        "cool": 0
    },
    "user_id": "SS85hfTApRnbTPcJadra8A",
    "review_id": "VyAKIaj_Rmsf_ZCHcGJyUw",
    "stars": 5,
    "date": "2010-05-30",
    "text": "I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.",
    "type": "review",
    "business_id": "70p94Ejeu1v5XlIkbKORYQ"
}"""}    
        context_dict["shortname"] = truncateName(context_dict["name"])
    else :
        context_dict = {"a" : a , "user": "Melissa", "name": "Chipotle Mexican Grill", "votes": {"funny": 0, "useful": 0, "cool": 0}, "user_id": "xAVu2pZ6nIvkdHh8vGs84Q", "review_id": "DusrkpkTGPGkqK13xO1TZg", "stars": 3, "date": "2011-11-26", "text": "Standard Chipotle fare - consistently good; not bad for corporate food - if you have a few minutes, there are a number of good local offerings within walking distance.", "type": "review", "business_id": "WcGTSRku3mrVK7V9GKq4UQ", "json" : """{
    "votes": {
        "funny": 0,
        "useful": 0,
        "cool": 0
    },
    "user_id": "xAVu2pZ6nIvkdHh8vGs84Q",
    "review_id": "DusrkpkTGPGkqK13xO1TZg",
    "stars": 3,
    "date": "2011-11-26",
    "text": "Standard Chipotle fare - consistently good; not bad for corporate food - if you have a few minutes, there are a number of good local offerings within walking distance.",
    "type": "review",
    "business_id": "WcGTSRku3mrVK7V9GKq4UQ"
}"""}
        context_dict["shortname"] = truncateName(context_dict["name"])
    return render_to_response('OperationRepo/review.html', context_dict, context)

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