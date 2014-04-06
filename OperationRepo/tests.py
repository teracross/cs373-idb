from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import dumps, loads
from django.test import TestCase

class API_Test(TestCase) :

    # -----
    # get all
    # -----
    def test_get_business(self) :
        request = Request("http://oprepo.apiary.io/api/business")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
            {
                "business_id": "O_X3PGhk3Y5JWVi866qlJg",
                "name": "Turf Paradise Race Course"
            },
            {
                "business_id": "QbrM7wqtmoNncqjc6GtFaQ",
                "name": "Sam's Club Members Only"
            }
        ]

        self.assertTrue(content == actual)


    def test_get_user(self) :
        request = Request("http://oprepo.apiary.io/api/user")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
            {
                "user_id": "2WyMjf6TYATFwg6NA",
                "name": "Glen"
            },
            {
                "business_id": "gYV6bmTSgbZMGkvXHVCowg",
                "name": "Paul"
            }
        ]

        self.assertTrue(content == actual)


    def test_get_review(self) :
        request = Request("http://oprepo.apiary.io/api/review")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
            {
                "user_id": "r-t7IiTSD0QZdt8lOUCqeQ",
                "review_id": "0ESSqLfOae77muWTv_zUqA",
                "business_id": "WIcDFpHEnC3ihNmS7-6-ZA"
            },
            {
                "user_id": "SS85hfTApRnbTPcJadra8A",
                "review_id": "VyAKIaj_Rmsf_ZCHcGJyUw",
                "business_id": "70p94Ejeu1v5XlIkbKORYQ"
            }
        ]

        self.assertTrue(content == actual)


    # -----
    # post
    # -----
    def test_post_business(self) :
        values = dumps({
            "business_id": "O_X3PGhk3Y5JWVi866qlJg",
            "full_address": "1501 W Bell Rd\nPhoenix, AZ 85023",
            "hours": {"Monday": {"close": "18:00", "open": "11:00"},
            "Tuesday": {"close": "18:00", "open": "11:00"},
            "Friday": {"close": "18:00", "open": "11:00"},
            "Wednesday": {"close": "18:00", "open": "11:00"},
            "Thursday": {"close": "18:00", "open": "11:00"},
            "Sunday": {"close": "18:00", "open": "11:00"},
            "Saturday": {"close": "18:00","open": "11:00"}},
            "open": True,
            "categories": ["Active Life", "Arts & Entertainment", "Stadiums & Arenas", "Horse Racing"],
            "city": "Phoenix",
            "review_count": 29,
            "name": "Turf Paradise Race Course",
            "neighborhoods": [],
            "longitude": -112.0923293,
            "state": "AZ",
            "stars": 4.0,
            "latitude": 33.638572699999997,
            "attributes": {"Take-out": False,
            "Wi-Fi": "free",
            "Good For": {"dessert": False,
            "latenight": False,
            "lunch": False,
            "dinner": False,
            "brunch": False,
            "breakfast": False},
            "Noise Level": "average",
            "Takes Reservations": True,
            "Has TV": True,
            "Delivery": False,
            "Ambience": {"romantic": False,
            "intimate": False,
            "touristy": False,
            "hipster": False,
            "divey": False,
            "classy": False,
            "trendy": False,
            "upscale": False,
            "casual": False},
            "Parking": {"garage": False,
            "street": False,
            "validated": False,
            "lot": True,
            "valet": True},
            "Wheelchair Accessible": True,
            "Outdoor Seating": True,
            "Attire": "casual",
            "Alcohol": "full_bar",
            "Waiter Service": True,
            "Accepts Credit Cards": True,
            "Good for Kids": False,
            "Good For Groups": True,
            "Price Range": 2},
            "type": "business"
        })
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/business", data=values.encode("utf-8"), headers=headers)
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"business_id\": \"O_X3PGhk3Y5JWVi866qlJg\" }")

    def test_post_user(self) :
        values = dumps({
            "yelping_since": "2011-08",
            "votes": {"funny": 0,
            "useful": 1,
            "cool": 1},
            "review_count": 5,
            "name": "Glen",
            "user_id": "HzLh-2WyMjf6TYATFwg6NA",
            "friends": [],
            "fans": 0,
            "average_stars": 3.6000000000000001,
            "type": "user",
            "compliments": {},
            "elite": []
        })
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/user", data=values.encode("utf-8"), headers=headers)
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"user_id\": \"HzLh-2WyMjf6TYATFwg6NA\" }")

    def test_post_review(self) :
        values = dumps({
            "votes": {"funny": 0,
            "useful": 0,
            "cool": 0},
            "user_id": "SS85hfTApRnbTPcJadra8A",
            "review_id": "VyAKIaj_Rmsf_ZCHcGJyUw",
            "stars": 5,
            "date": "2010-05-30",
            "text": "I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.",
            "type": "review",
            "business_id": "70p94Ejeu1v5XlIkbKORYQ"
        })
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/review", data=values.encode("utf-8"), headers=headers)
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"review_id\": \"VyAKIaj_Rmsf_ZCHcGJyUw\" }")


    # -----
    # get single
    # -----
    def test_get_business_single(self) :
        request = Request("http://oprepo.apiary.io/api/business/{id}")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = {'state': 'AZ', 'hours': {'Sunday': {'close': '18:00', 'open': '11:00'}, 'Monday': {'close': '18:00', 'open': '11:00'}, 'Tuesday': {'close': '18:00', 'open': '11:00'}, 'Friday': {'close': '18:00', 'open': '11:00'}, 'Saturday': {'close': '18:00', 'open': '11:00'}, 'Thursday': {'close': '18:00', 'open': '11:00'}, 'Wednesday': {'close': '18:00', 'open': '11:00'}}, 'stars': 4.0, 'full_address': '1501 W Bell Rd\nPhoenix, AZ 85023', 'latitude': 33.6385727, 'attributes': {'takes_reservations': True, 'parking': {'street': False, 'garage': False, 'lot': True, 'valet': True, 'validated': False}, 'price_range': 2, 'ambience': {'classy': False, 'divey': False, 'touristy': False, 'hipster': False, 'romantic': False, 'casual': False, 'trendy': False, 'upscale': False, 'intimate': False}, 'alcohol': 'full_bar', 'waiter_service': True, 'delivery': False, 'has_tv': True, 'take_out': False, 'accepts_credit_cards': True, 'noise_level': 'average', 'wifi': 'free', 'outdoor_seating': True, 'wheelchair_accessible': True, 'good_for_groups': True, 'good_for': {'dinner': False, 'breakfast': False, 'lunch': False, 'brunch': False, 'dessert': False, 'latenight': False}, 'good_for_kids': False, 'attire': 'casual'}, 'categories': ['Active Life', 'Arts & Entertainment', 'Stadiums & Arenas', 'Horse Racing'], 'open': True, 'city': 'Phoenix', 'neighborhoods': [], 'type': 'business', 'review_count': 29, 'name': 'Turf Paradise Race Course', 'longitude': -112.0923293, 'business_id': 'O_X3PGhk3Y5JWVi866qlJg'}
        self.assertTrue(content == actual)


    def test_get_user_single(self) :
        request = Request("http://oprepo.apiary.io/api/user/{id}")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = {
            "yelping_since": "2011-08",
            "votes": {"funny": 0,
                    "useful": 1,
                    "cool": 1},
            "review_count": 5,
            "name": "Glen",
            "user_id": "HzLh-2WyMjf6TYATFwg6NA",
            "friends": [],
            "fans": 0,
            "average_stars": 3.6000000000000001,
            "type": "user",
            "compliments": {},
            "elite": []
        }
        self.assertTrue(content == actual)


    def test_get_review_single(self) :
        request = Request("http://oprepo.apiary.io/api/review/{id}")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = {
            "votes": {"funny": 0,
                    "useful": 0,
                    "cool": 0},
            "user_id": "SS85hfTApRnbTPcJadra8A",
            "review_id": "VyAKIaj_Rmsf_ZCHcGJyUw",
            "stars": 5,
            "date": "2010-05-30",
            "text": "I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.",
            "type": "review",
            "business_id": "70p94Ejeu1v5XlIkbKORYQ"
        }
        self.assertTrue(content == actual)


    # -----
    # delete
    # -----
    def test_delete_business(self) :
        request = Request("http://oprepo.apiary.io/api/business/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)

        self.assertTrue(response.getcode(), 204)


    def test_delete_user(self) :
        request = Request("http://oprepo.apiary.io/api/user/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)

        self.assertTrue(response.getcode(), 204)


    def test_delete_review(self) :
        request = Request("http://oprepo.apiary.io/api/review/{id}")
        request.get_method = lambda: 'DELETE'
        response = urlopen(request)

        self.assertTrue(response.getcode(), 204)


    # -----
    # get review for business
    # -----
    def test_get_business_review(self) :
        request = Request("http://oprepo.apiary.io/api/business/{id}/review")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
    {
        "votes": {"funny": 0,
                "useful": 1,
                "cool": 0},
        "user_id": "oexyVjQSZ62qT7tpxgOcKg",
        "review_id": "s8g8kFZ4JXFAGksbQnEqLw",
        "stars": 4,
        "date": "2012-01-07",
        "text": "I have never been to a race track before so when I saw a Livingsocial deal for this place I thought I'd try it out. It was the best $30 I ever spent! We sat in the Turf Club which I guess is the nicest viewing area. There wasn't a bad table in the place, even the 2 tops which is what we had. The menu is mostly lunch type items, salad, sandwiches, burgers, with a few breakfast options, but the food was surprisingly good and very reasonably priced. I had the tuna melt and it was stuffed with tuna salad and cheese. The BF had the chicken caprese sandwich. The sandwich arrived, I looked up a second later and it was gone. He inhaled it,  he thought it was that good. The bread pudding was ok. The only thing that wasn't awesome was the service. Our waitress was very slow to come around and she didn't have much of a personality. Any time we needed anything I had to flag her down but who knows it could have been an off day for her. We walked around and went to the grandstand and outside viewing area as well. There are stadium type food booths and a couple of bars out there and it looked fun. We would definitely go back again and pay the full price. So worth it.",
        "type": "review",
        "business_id": "O_X3PGhk3Y5JWVi866qlJg"
    }
]
        self.assertTrue(content == actual)


    # -----
    # get user who reviewed business
    # -----
    def test_get_business_user(self) :
        request = Request("http://oprepo.apiary.io/api/business/{id}/user")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
    {
        "yelping_since": "2008-04",
        "votes": {"funny": 25,
                "useful": 122,
                "cool": 31},
        "review_count": 69,
        "name": "Mindi",
        "user_id": "oexyVjQSZ62qT7tpxgOcKg",
        "friends": ["OroGqv0t7fy-Q3E2PzTEwQ", "SEDFpR4oMPKqXMjbJiMGog", "AYGHNy8gPxl2Q-etTT3hZw", "34gJ_KlP3RM6jotNT6TcDQ", "fHv7k5vWd6ryt8jH4J3teg", "lmiDCrmas8TxRsbIGZX9Pg", "Ts2ipR4zCYClEQTAuJuIjw", "4SFf4irFi5s8Q4QIxFhvUQ"],
        "fans": 1,
        "average_stars": 3.5800000000000001,
        "type": "user",
        "compliments": {"note": 4,
                    "funny": 1,
                    "writer": 3,
                    "cool": 2},
        "elite": []
    }
]

        self.assertTrue(content == actual)


    # -----
    # get business reviewed by user
    # -----
    def test_get_user_business(self) :
        request = Request("http://oprepo.apiary.io/api/user/{id}/business")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [{'full_address': '3701-3965 Sky Harbor Blvd\nPhoenix, AZ 85034', 'latitude': 33.4336774955193, 'categories': ['Bakeries', 'Food', 'French', 'Restaurants'], 'type': 'business', 'longitude': -112.001445002113, 'name': 'La Madeleine', 'state': 'AZ', 'city': 'Phoenix', 'neighborhoods': [], 'attributes': {'good_for': {'dessert': False, 'latenight': False, 'breakfast': False, 'lunch': False, 'dinner': False, 'brunch': False}, 'accepts_credit_cards': True, 'delivery': False, 'wifi': 'free', 'outdoor_seating': False, 'attire': 'casual', 'waiter_service': False}, 'review_count': 12, 'business_id': 'KWo4geULVPzCirc0Scpcow', 'open': True, 'hours': {}, 'stars': 3.5}]
        self.assertTrue(content == actual)


    # -----
    # get review by user
    # -----
    def test_get_user_review(self) :
        request = Request("http://oprepo.apiary.io/api/user/{id}/review")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
    {
        "votes": {"funny": 0,
                "useful": 1,
                "cool": 1},
        "user_id": "HzLh-2WyMjf6TYATFwg6NA",
        "review_id": "q2H0J8iJvwUgINvUb8L5Bw",
        "stars": 1,
        "date": "2013-12-08",
        "text": "Epic fail. So I order a sandwich that clearly says it comes with Pesto on it, and instead comes drowned in mayo. So I take it back to the counter, point out the error and they take it back. I hear the manager correcting the staff, who mouths off to him. The manager comes back and says that the fixed sandwich will be right back out. They give me the same sandwich, with all the mayo still on it and a gallon of pink goo which I assume is the tomato Pesto. Not going back again. What a waste.",
        "type": "review",
        "business_id": "KWo4geULVPzCirc0Scpcow"
    }
]
        self.assertTrue(content == actual)


    # -----
    # get business from review
    # -----
    def test_get_review_business(self) :
        request = Request("http://oprepo.apiary.io/api/review/{id}/business")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [{'latitude': 33.3790657, 'attributes': {'wheelchair_accessible': True, 'accepts_credit_cards': True, 'parking': {'street': False, 'valet': False, 'validated': False, 'lot': True, 'garage': False}, 'by_appointment_only': True, 'price_range': 2, 'good_for_kids': True}, 'stars': 5.0, 'categories': ['Hair Salons', 'Beauty & Spas'], 'open': True, 'state': 'AZ', 'business_id': '70p94Ejeu1v5XlIkbKORYQ', 'longitude': -111.7556025, 'city': 'Gilbert', 'hours': {'Thursday': {'close': '19:00', 'open': '09:00'}, 'Saturday': {'close': '19:00', 'open': '09:00'}, 'Monday': {'close': '19:00', 'open': '09:00'}, 'Wednesday': {'close': '19:00', 'open': '09:00'}, 'Tuesday': {'close': '19:00', 'open': '09:00'}, 'Friday': {'close': '19:00', 'open': '09:00'}}, 'type': 'business', 'review_count': 9, 'name': 'Salon Lola', 'full_address': '3479 E Baseline Rd\nSte 18\nGilbert, AZ 85234', 'neighborhoods': []}]
        self.assertTrue(content == actual)


    # -----
    # get user from review
    # -----
    def test_get_review_user(self) :
        request = Request("http://oprepo.apiary.io/api/review/{id}/user")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [
    {
        "yelping_since": "2010-05",
        "votes": {"funny": 0,
                "useful": 4,
                "cool": 0},
        "review_count": 1,
        "name": "Christi",
        "user_id": "SS85hfTApRnbTPcJadra8A",
        "friends": [],
        "fans": 0,
        "average_stars": 5.0,
        "type": "user",
        "compliments": {},
        "elite": []
    }
]

        self.assertTrue(content == actual)


    # -----
    # put
    # -----
    def test_put_business(self) :
        values = "{ \n    \"business_id\": \"O_X3PGhk3Y5JWVi866qlJg\",\n    \"full_address\": \"1501 W Bell Rd\\nPhoenix, AZ 85023\",\n    \"hours\": {\"Monday\": {\"close\": \"18:00\", \"open\": \"11:00\"},\n            \"Tuesday\": {\"close\": \"18:00\", \"open\": \"11:00\"},\n            \"Friday\": {\"close\": \"18:00\", \"open\": \"11:00\"},\n            \"Wednesday\": {\"close\": \"18:00\", \"open\": \"11:00\"},\n            \"Thursday\": {\"close\": \"18:00\", \"open\": \"11:00\"}, \n            \"Sunday\": {\"close\": \"18:00\", \"open\": \"11:00\"},\n            \"Saturday\": {\"close\": \"18:00\",\"open\": \"11:00\"}},\n    \"open\": true,\n    \"categories\": [\"Active Life\", \"Arts \u0026 Entertainment\", \"Stadiums \u0026 Arenas\", \"Horse Racing\"],\n    \"city\": \"Phoenix\",\n    \"review_count\": 29,\n    \"name\": \"Turf Paradise Race Course\",\n    \"neighborhoods\": [],\n    \"longitude\": -112.0923293,\n    \"state\": \"AZ\",\n    \"stars\": 4.0,\n    \"latitude\": 33.638572699999997,\n    \"attributes\": {\"Take-out\": false,\n                \"Wi-Fi\": \"free\",\n                \"Good For\": {\"dessert\": false,\n                            \"latenight\": false,\n                            \"lunch\": false,\n                            \"dinner\": false,\n                            \"brunch\": false,\n                            \"breakfast\": false},\n                \"Noise Level\": \"average\",\n                \"Takes Reservations\": true,\n                \"Has TV\": true,\n                \"Delivery\": false,\n                \"Ambience\": {\"romantic\": false,\n                            \"intimate\": false,\n                            \"touristy\": false,\n                            \"hipster\": false,\n                            \"divey\": false,\n                            \"classy\": false,\n                            \"trendy\": false,\n                            \"upscale\": false,\n                            \"casual\": false},\n                \"Parking\": {\"garage\": false,\n                            \"street\": false,\n                            \"validated\": false,\n                            \"lot\": true,\n                            \"valet\": true},\n                \"Wheelchair Accessible\": true,\n                \"Outdoor Seating\": true,\n                \"Attire\": \"casual\",\n                \"Alcohol\": \"full_bar\",\n                \"Waiter Service\": true,\n                \"Accepts Credit Cards\": true,\n                \"Good for Kids\": false,\n                \"Good For Groups\": true,\n                \"Price Range\": 2},\n    \"type\": \"business\"\n}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/business/{id}", data=values.encode("utf-8"), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        self.assertTrue(response.getcode() == 204)


    def test_put_user(self) :
        values = "{ \n    \"yelping_since\": \"2011-08\",\n    \"votes\": {\"funny\": 0,\n            \"useful\": 1,\n            \"cool\": 1},\n    \"review_count\": 5,\n    \"name\": \"Glen\",\n    \"user_id\": \"HzLh-2WyMjf6TYATFwg6NA\",\n    \"friends\": [],\n    \"fans\": 0,\n    \"average_stars\": 3.6000000000000001,\n    \"type\": \"user\",\n    \"compliments\": {},\n    \"elite\": [],\n}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/user/{id}", data=values.encode("utf-8"), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        self.assertTrue(response.getcode() == 204)


    def test_put_review(self) :
        values = "{ \n    \"votes\": {\"funny\": 0,\n            \"useful\": 0,\n            \"cool\": 0},\n    \"user_id\": \"SS85hfTApRnbTPcJadra8A\",\n    \"review_id\": \"VyAKIaj_Rmsf_ZCHcGJyUw\",\n    \"stars\": 5,\n    \"date\": \"2010-05-30\",\n    \"text\": \"I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.\",\n    \"type\": \"review\",\n    \"business_id\": \"70p94Ejeu1v5XlIkbKORYQ\"\n}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://oprepo.apiary.io/api/review/{id}", data=values.encode("utf-8"), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        response_body = response.read()
        self.assertTrue(response.getcode() == 204)


    #---
    #api get tests
    #---
    def test_api_get_all_business(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  [{"attributes": {"accepts_credit_cards": "true", "alcohol": "full_bar", "ambience": "{'trendy': false, 'classy': false, 'hipster': false, 'romantic': false, 'divey': false, 'intimate': false, 'upscale': false, 'touristy': false, 'casual': true}", "attire": "casual", "coat_check": "false", "delivery": "false", "good_for": "{'latenight': false, 'lunch': true, 'brunch': false, 'dinner': true, 'breakfast': false, 'dessert': true}", "good_for_dancing": "false", "good_for_groups": "true", "good_for_kids": "true", "happy_hour": "true", "has_tv": "true", "music": "{'dj': false, 'karaoke': false, 'live': false, 'video': false, 'jukebox': false, 'background_music': true}", "noise_level": "very_loud", "outdoor_seating": "true", "parking": "{'lot': true, 'valet': false, 'validated': false, 'street': false, 'garage': false}", "price_range": "2", "smoking": "outdoor", "takeout": "true", "takes_reservations": "false", "waiter_service": "true", "wheelchair_accessible": "true", "wifi": "free"}, "business_id": "00eGk1ntf4RiDxVRY3gaIw", "categories": ["Restaurants", "Salad", "Pizza", "American (Traditional)"], "city": "Mesa", "hours": {"Friday": {"close": "02:00:00", "open": "11:00:00"}, "Monday": {"close": "02:00:00", "open": "11:00:00"}, "Saturday": {"close": "02:00:00", "open": "11:00:00"}, "Sunday": {"close": "02:00:00", "open": "11:00:00"}, "Thursday": {"close": "02:00:00", "open": "11:00:00"}, "Tuesday": {"close": "02:00:00", "open": "11:00:00"}, "Wednesday": {"close": "02:00:00", "open": "11:00:00"}}, "name": "Old Chicago", "neighborhoods": []}, {"attributes": {}, "business_id": "00FGafv0TKfmH_QhVxh4FQ", "categories": ["Car Dealers", "RV Dealers", "Automotive"], "city": "Surprise", "hours": {"Friday": {"close": "17:00:00", "open": "08:30:00"}, "Saturday": {"close": "17:00:00", "open": "08:30:00"}, "Thursday": {"close": "17:00:00", "open": "08:30:00"}, "Tuesday": {"close": "17:00:00", "open": "08:30:00"}, "Wednesday": {"close": "17:00:00", "open": "08:30:00"}}, "name": "Tom's Camperland", "neighborhoods": []}, {"attributes": {"accepts_credit_cards": "true", "parking": "{'lot': true, 'valet': false, 'validated': false, 'street': false, 'garage': false}", "price_range": "2", "wifi": "no"}, "business_id": "015GCpe-tMj1En4NORROzA", "categories": ["Dry Cleaning & Laundry", "Local Services"], "city": "Phoenix", "hours": {"Friday": {"close": "19:00:00", "open": "07:00:00"}, "Monday": {"close": "19:00:00", "open": "07:00:00"}, "Saturday": {"close": "18:00:00", "open": "09:00:00"}, "Thursday": {"close": "19:00:00", "open": "07:00:00"}, "Tuesday": {"close": "19:00:00", "open": "07:00:00"}, "Wednesday": {"close": "19:00:00", "open": "07:00:00"}}, "name": "Elite Cleaners", "neighborhoods": []}, {"attributes": {"accepts_credit_cards": "true", "alcohol": "full_bar", "ambience": "{'trendy': false, 'classy': false, 'hipster': false, 'romantic': false, 'divey': false, 'intimate': false, 'upscale': false, 'touristy': false, 'casual': true}", "coat_check": "false", "delivery": "false", "good_for": "{'latenight': false, 'lunch': false, 'brunch': false, 'dinner': false, 'breakfast': false, 'dessert': false}", "good_for_dancing": "false", "good_for_groups": "true", "happy_hour": "true", "has_tv": "true", "music": "{'dj': false, 'karaoke': false, 'live': false, 'video': false, 'jukebox': false, 'background_music': true}", "noise_level": "average", "outdoor_seating": "true", "parking": "{'lot': true, 'valet': false, 'validated': false, 'street': false, 'garage': false}", "price_range": "2", "smoking": "outdoor", "takeout": "true", "takes_reservations": "false", "waiter_service": "true", "wheelchair_accessible": "true"}, "business_id": "01cEFI5Pq_RyEwM3GSTopQ", "categories": ["Nightlife", "Sports Bars", "Bars"], "city": "Scottsdale", "hours": {"Friday": {"close": "23:00:00", "open": "11:00:00"}, "Monday": {"close": "22:00:00", "open": "11:00:00"}, "Saturday": {"close": "23:00:00", "open": "11:00:00"}, "Sunday": {"close": "22:00:00", "open": "11:00:00"}, "Thursday": {"close": "22:00:00", "open": "11:00:00"}, "Tuesday": {"close": "22:00:00", "open": "11:00:00"}, "Wednesday": {"close": "22:00:00", "open": "11:00:00"}}, "name": "Blue 32 Sports Grill", "neighborhoods": []}, {"attributes": {}, "business_id": "01cQQpeEwWpzTgv6YUQhAQ", "categories": ["Beauty & Spas", "Hair Salons"], "city": "Glendale", "hours": {}, "name": "Mario's Hair Company", "neighborhoods": []}, {"attributes": {"accepts_credit_cards": "true", "alcohol": "none", "ambience": "{'trendy': false, 'classy': false, 'hipster': false, 'romantic': false, 'divey': false, 'intimate': false, 'upscale': false, 'touristy': false, 'casual': false}", "attire": "casual", "caters": "false", "delivery": "false", "drivethru": "false", "good_for": "{'latenight': false, 'lunch': false, 'brunch': false, 'dinner': false, 'breakfast': false, 'dessert': false}", "good_for_groups": "true", "good_for_kids": "true", "has_tv": "true", "noise_level": "quiet", "outdoor_seating": "true", "parking": "{'lot': false, 'valet': false, 'validated': false, 'street': false, 'garage': false}", "price_range": "1", "takeout": "true", "takes_reservations": "false", "waiter_service": "false", "wifi": "no"}, "business_id": "01euuGhBwvcDhl9KcPTang", "categories": ["Restaurants", "Mexican", "Fast Food", "Breakfast & Brunch"], "city": "Mesa", "hours": {"Friday": {"close": "03:00:00", "open": "08:00:00"}, "Monday": {"close": "00:00:00", "open": "08:00:00"}, "Saturday": {"close": "03:00:00", "open": "08:00:00"}, "Sunday": {"close": "00:00:00", "open": "08:00:00"}, "Thursday": {"close": "00:00:00", "open": "08:00:00"}, "Tuesday": {"close": "00:00:00", "open": "08:00:00"}, "Wednesday": {"close": "00:00:00", "open": "08:00:00"}}, "name": "El Salsita", "neighborhoods": []}, {"attributes": {}, "business_id": "01kU7NKzfCP3tgYmgzXbjQ", "categories": [], "city": "Surprise", "hours": {}, "name": "Water Fountain", "neighborhoods": []}, {"attributes": {"good_for_kids": "true"}, "business_id": "022T8YSRmb3b1BfwzO3F7Q", "categories": ["Bowling", "Active Life"], "city": "Scottsdale", "hours": {}, "name": "Brunswick Via Linda Lanes", "neighborhoods": []}, {"attributes": {}, "business_id": "02Fijjr_ccD42E-5aGOXWQ", "categories": ["Carpet Cleaning", "Local Services"], "city": "Phoenix", "hours": {}, "name": "Pure Air Service Arizona", "neighborhoods": []}, {"attributes": {"accepts_credit_cards": "true", "dogs_allowed": "true", "outdoor_seating": "true", "takes_reservations": "true", "wheelchair_accessible": "true"}, "business_id": "02rrDia_FTc8jN7LGqzIbQ", "categories": ["Restaurants", "Horseback Riding", "Barbeque", "Active Life"], "city": "Goodyear", "hours": {"Friday": {"close": "21:00:00", "open": "10:00:00"}, "Saturday": {"close": "21:00:00", "open": "10:00:00"}, "Sunday": {"close": "18:00:00", "open": "10:00:00"}, "Thursday": {"close": "20:00:00", "open": "10:00:00"}, "Wednesday": {"close": "20:00:00", "open": "10:00:00"}}, "name": "Corral West Arena", "neighborhoods": []}]
        self.assertTrue(content==actual)

    def test_api_get_business(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/00eGk1ntf4RiDxVRY3gaIw/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  {"attributes": {"accepts_credit_cards": "true", "alcohol": "full_bar", "ambience": "{'trendy': false, 'classy': false, 'hipster': false, 'romantic': false, 'divey': false, 'intimate': false, 'upscale': false, 'touristy': false, 'casual': true}", "attire": "casual", "coat_check": "false", "delivery": "false", "good_for": "{'latenight': false, 'lunch': true, 'brunch': false, 'dinner': true, 'breakfast': false, 'dessert': true}", "good_for_dancing": "false", "good_for_groups": "true", "good_for_kids": "true", "happy_hour": "true", "has_tv": "true", "music": "{'dj': false, 'karaoke': false, 'live': false, 'video': false, 'jukebox': false, 'background_music': true}", "noise_level": "very_loud", "outdoor_seating": "true", "parking": "{'lot': true, 'valet': false, 'validated': false, 'street': false, 'garage': false}", "price_range": "2", "smoking": "outdoor", "takeout": "true", "takes_reservations": "false", "waiter_service": "true", "wheelchair_accessible": "true", "wifi": "free"}, "business_id": "00eGk1ntf4RiDxVRY3gaIw", "categories": ["Restaurants", "Salad", "Pizza", "American (Traditional)"], "city": "Mesa", "hours": {"Friday": {"close": "02:00:00", "open": "11:00:00"}, "Monday": {"close": "02:00:00", "open": "11:00:00"}, "Saturday": {"close": "02:00:00", "open": "11:00:00"}, "Sunday": {"close": "02:00:00", "open": "11:00:00"}, "Thursday": {"close": "02:00:00", "open": "11:00:00"}, "Tuesday": {"close": "02:00:00", "open": "11:00:00"}, "Wednesday": {"close": "02:00:00", "open": "11:00:00"}}, "name": "Old Chicago", "neighborhoods": []}
        self.assertTrue(content==actual)

    def test_api_get_bad_business(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/nothere/")
        try :
            response = urlopen(request)
        except HTTPError :
            return True
        return False

    def test_api_get_all_users(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  [{"compliments": {}, "name": "lisa", "user_id": "x5-yK8bmjQTcMrlWLfgJEg", "votes": {"cool": 1, "funny": 3, "useful": 4}}, {"compliments": {"funny": 1, "plain": 3}, "name": "Amanda", "user_id": "Ae_rbQ293MYrKaywJT6Oeg", "votes": {"cool": 0, "funny": 11, "useful": 12}}, {"compliments": {"cool": 1, "more": 1}, "name": "Brian", "user_id": "8EaO99Q3E_SS8KzOR1rFrA", "votes": {"cool": 7, "funny": 4, "useful": 35}}, {"compliments": {}, "name": "Paul", "user_id": "EsZoGB023YUubq7rC7rm8Q", "votes": {"cool": 2, "funny": 2, "useful": 5}}, {"compliments": {}, "name": "Peter", "user_id": "fdnSC-PGo2mYTgcOEq6Bpw", "votes": {"cool": 0, "funny": 0, "useful": 4}}, {"compliments": {"cool": 158, "cute": 4, "funny": 42, "hot": 147, "list": 15, "more": 11, "note": 80, "photos": 11, "plain": 103, "profile": 5, "writer": 43}, "elite": 2008, "name": "Michael", "user_id": "90a6z--_CUrl84aCzZyPsg", "votes": {"cool": 2384, "funny": 1440, "useful": 3240}}, {"compliments": {}, "name": "Scooter", "user_id": "egm1AgWT-cttbm4nu_FVcQ", "votes": {"cool": 2, "funny": 2, "useful": 12}}, {"compliments": {}, "name": "marty", "user_id": "eqHh3T-QWN8bowagW4KiGg", "votes": {"cool": 5, "funny": 12, "useful": 46}}, {"compliments": {}, "name": "Kris", "user_id": "KbmjlHxkj4dA8t90IWjgpQ", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"compliments": {}, "name": "Ingrid", "user_id": "a8Xp9eCcmtWKhnlB5V4Ghg", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"compliments": {}, "name": "Kate", "user_id": "NFaCr9xvyDBioc2mB1w08w", "votes": {"cool": 1, "funny": 0, "useful": 2}}, {"compliments": {"cool": 2}, "name": "Erin", "user_id": "bZaSmDxmKbVNOOAdzxX_bg", "votes": {"cool": 6, "funny": 2, "useful": 13}}, {"compliments": {}, "name": "John", "user_id": "wBi0I2QcqZtNOh21WlBVKA", "votes": {"cool": 46, "funny": 356, "useful": 127}}, {"compliments": {"cool": 5, "funny": 1, "hot": 6, "more": 1, "note": 7, "plain": 20, "writer": 5}, "elite": 2014, "name": "Ricky", "user_id": "yWBwbPCOy8eBD1wWSH6s_A", "votes": {"cool": 69, "funny": 42, "useful": 271}}, {"compliments": {"cool": 42, "cute": 1, "funny": 7, "hot": 19, "more": 2, "note": 21, "photos": 2, "plain": 42, "writer": 5}, "elite": 2014, "name": "Patrick", "user_id": "Kqvfep2mxS10S50FbVDi4Q", "votes": {"cool": 310, "funny": 188, "useful": 600}}, {"compliments": {"cute": 1}, "name": "Steven", "user_id": "EVSAweqdsY_EWfDxqDYdDg", "votes": {"cool": 0, "funny": 0, "useful": 1}}, {"compliments": {"note": 2}, "name": "Michael", "user_id": "GjNyOTcibcI_XKCzeMgO2g", "votes": {"cool": 6, "funny": 7, "useful": 21}}, {"compliments": {"cool": 82, "funny": 15, "hot": 38, "list": 1, "more": 1, "note": 38, "photos": 5, "plain": 118, "profile": 2, "writer": 35}, "elite": 2014, "name": "Floyd", "user_id": "SEDFpR4oMPKqXMjbJiMGog", "votes": {"cool": 818, "funny": 414, "useful": 1281}}, {"compliments": {"cool": 47, "cute": 2, "funny": 22, "hot": 34, "more": 5, "note": 29, "photos": 3, "plain": 41, "profile": 2, "writer": 11}, "elite": 2014, "name": "Tasia", "user_id": "fl6oI21uXoxVMwfR6lFanQ", "votes": {"cool": 307, "funny": 318, "useful": 532}}, {"compliments": {"cool": 16, "funny": 8, "hot": 21, "list": 1, "more": 3, "note": 4, "plain": 12, "writer": 6}, "elite": 2013, "name": "Christopher", "user_id": "nbofxFWHORebBHh10OgYLA", "votes": {"cool": 187, "funny": 216, "useful": 335}}]
        self.assertTrue(content==actual)

    def test_api_get_user(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/x5-yK8bmjQTcMrlWLfgJEg/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  {"compliments": {}, "name": "lisa", "user_id": "x5-yK8bmjQTcMrlWLfgJEg", "votes": {"cool": 1, "funny": 3, "useful": 4}}
        self.assertTrue(content==actual)

    def test_api_get_bad_user(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/nothere/")
        try :
            response = urlopen(request)
        except HTTPError :
            return True
        return False

    def test_api_get_all_reviews(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  [{"business": "/operationrepo/api/business/022T8YSRmb3b1BfwzO3F7Q/", "date": "2011-01-12", "review_id": "rGWvvzfxIv-aoAKGGGHrMg", "stars": 4.0, "text": "Fun place! We've mostly just been here for our league's cosmic bowling nights. It's a fun place to socialize and have fun with your friends. The prices are good too!", "user": "/operationrepo/api/user/xFG4Ca2HHmbxDTkMlmHnjQ/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/00eGk1ntf4RiDxVRY3gaIw/", "date": "2013-08-03", "review_id": "UenRro_ZUAW7vmbS9Hoqrg", "stars": 3.0, "text": "Not a bad place if you like craft beers. I came in to start another mini tour. I always love the food especially the pizza. The service is usually good, however today it sucked. We were seated at the bar 10 minutes before we were greeted by the bartender.  Not a full bar either. The food we ordered was out in a reasonable time and was delicious. My only issue today was with the bartender and the service we got. If I go there again and see her tending I will go to the restaurant part.", "user": "/operationrepo/api/user/icf8Tr75xv-QOnI7wZX9Xw/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/015GCpe-tMj1En4NORROzA/", "date": "2013-10-17", "review_id": "3fhIpynSC-C5NVEjZO-QYg", "stars": 4.0, "text": "I had no problem redeeming the 30-50 coupon. The staff was very friendly and knowledgeable. \nThe clothes came out clean, except one that said they couldn't take the stains off without damaging the item, that item was charge which I don't think it should; since it was not cleaned. \nThe price on my personal opinion it's very expensive. I took 11 pieces and paid with coupon over \\$80.", "user": "/operationrepo/api/user/EbAgR_Lmwr6-kut0bRhV-g/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/00eGk1ntf4RiDxVRY3gaIw/", "date": "2011-08-26", "review_id": "LcEP4Jc8ajplPSdHfiP50A", "stars": 2.0, "text": "Seriously the only reason it is getting two stars tonight is because they have snakebites.\n\nNow I will be the first to say that I frequent Old Chicago quite often, but tonight was down right depressing. The bar area was about 29 degrees warmer than an oven baking cookies, and myself and date were downright sweating at the table. \n\nOrdered two beers, one (mine) perfect, the other was super flat; our waitress was super sweet and took care of it right away, but only after letting us know that the second choice was out.\n\nI will for sure be back to give it one more shot, but it was truly a HUGE disappointment tonight; especially when we were there to enjoy a cool night in with a draft.", "user": "/operationrepo/api/user/CjVX1QGNqx3_oDBuRig4-A/", "votes": {"cool": 0, "funny": 0, "useful": 1}}, {"business": "/operationrepo/api/business/01euuGhBwvcDhl9KcPTang/", "date": "2011-12-30", "review_id": "_VBQ9imkoKh0dsEiDUj8tA", "stars": 4.0, "text": "Love their tortas! They toast their bread so they're not soggy like most places. They also use a good amount of avacado and their prices are low.  They kinda of take a long time to prep the tortas tho. I only order from the drive-thru so I haven't been inside but it looks pretty clean from the outside.", "user": "/operationrepo/api/user/vArhfZStEAv8is9SM_YOOQ/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2010-11-22", "review_id": "rPp8OWlpQX08pmaHGjsxKw", "stars": 4.0, "text": "Was in Scottsdale for an overnight trip and decided to stop by this place to have some dinner and watch the Suns vs Lakers game.  The joint is a really nice sports bar and grill....I've never been to a sports bar that was so nice before, I thought I had the wrong place when I arrived.  The restaurant is well kept and looks like it just opened, at least by the cleanliness and decor.\n\nSince I was alone, I saddled up to the bar and decided to eat and have a few Beers while I watched the game.  The menu is pretty extensive, so I asked the bartender for her recommendation.  She suggested the Boneless Wings (\\$7.99) or the Sliders (\\$7.99 + \\$.50 w/Cheese).....I said, \"What the hell, let's go for both!\".  I asked her to make sure the Boneless Wings were really Spicy.  Since I had been in China for the past 10 days I was in the mood for some heat.....she said that their hottest wing sauce wasn't that hot....but that the cooks could whip up  a Habanero Sauce for me.  I asked her to have the Boneless Wings prepared with Hot Sauce and put the Habanero Sauce on the side, just to be on the safe side, LOL.  To wash it down, I had a 22 oz SunUp Trooper IPA (\\$5.50).\n\nI watched the Lakers vs Suns game for a while and made some new friends at the bar while I waited for my food.  After a short wait the first dish to come out was the Boneless Wings.  The Habanero Sauce was so Hot that when they placed it down in front of me I choked on the fumes....and this was with the Sauce on the Side!  I had to move the plate off to the side, just so I could breathe....perfect!  I took one piece of Boneless Wing, dipped it into the Habanero Sauce, and took a bite....wow, it packed a big punch!  Very spicy and soooo good!  The Chicken was moist and juicy and cooked just right.....not too crunchy and not too soft....and full of flavor.\n\nThe Sliders came out a few minutes later....so I left 1/2 my Wing order to go try the Sliders.  There were 4 Sliders on the plate.  I tried it with a little Blue Cheese Dressing.....yum!  Then I dipped them in a little Blue Cheese then with the Habanero Sauce that came with the Wings....even better!  I told the bartender to tell the cooks that their Habanero Sauce was a huge hit and to thank them for me.\n\nIt took me a while, but I devoured everything I ordered.  2 IPA's later and with a Lakers' loss in the making, I asked the bartender to change up the Beer order and asked for her recommendation.  She suggested the 4 Peaks Peach Ale (22 oz \\$5.50)....ok, I normally don't do Peach flavored Beer but went with it anyway.  I'm glad I did, it had a nice smooth finish and you could barely taste the Peach flavor....it didn't overwhelm the brew.\n\nDespite a Lakers loss, I had a great time and meal here.  Kudos to the staff for making a patron happy by whipping up a spicy Habanero Sauce on the fly....you can almost feel the heat in the pics I took.\n\nWill I return?  You bet I will!", "user": "/operationrepo/api/user/kGgAARL2UmvCcTRfiscjug/", "votes": {"cool": 7, "funny": 4, "useful": 6}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2010-08-04", "review_id": "WSEPR6x1xmdst6pe8imQ7g", "stars": 4.0, "text": "I can tell this is going to become a great local hangout (they just opened up two weeks ago). We visited on Monday night with some friends. The vibe is \"upscale sports grill\" with lots of flat TVs, a marble bar top, and fine furnishings throughout. I was very impressed with their service and the food, everything the four of us ordered was done just right. I'm looking forward to spending more quality time hanging at Blue 32!", "user": "/operationrepo/api/user/90a6z--_CUrl84aCzZyPsg/", "votes": {"cool": 3, "funny": 2, "useful": 4}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2011-08-29", "review_id": "bmOg5OJg4EMdTa2voSKEBg", "stars": 4.0, "text": "I was pleasantly surprised at this sports bar. Not your typical bar-food menu - though plenty of those staples as well. The menu was a bit longer than most sports bar type establishments, and varied. I had the grilled shrimp w/ rice and broccoli which sounds incredibly boring and possibly bland - it was neither. Grilled shrimp can easily come out dry and/or rubbery and this dish was tender, flavorful and the rice was flavored with a cilantro lime sauce. So yummy! My husband had Buffalo chicken sandwich that he ooohed and aahed over, so I guess he loved it. \n\nI was pleased to be able to get a decent wine by the glass! They also offer many specialty cocktails in addition to beer (of course). \n\nSpacious, modern decor. Lots of big booths, plenty of seating and many large TVs for those of you specifically looking for a place to watch the game. \n\nAlso, the server was a new trainee who clearly had worked in restaurants before because she displayed absolutely no \"Newness\" and her trainer was helpful and attentive as well.", "user": "/operationrepo/api/user/cl9ZMopdCQGGXMlwgruFdg/", "votes": {"cool": 0, "funny": 0, "useful": 1}}, {"business": "/operationrepo/api/business/022T8YSRmb3b1BfwzO3F7Q/", "date": "2011-07-13", "review_id": "Nhxu5YD1O3NbQ00fmioKWg", "stars": 2.0, "text": "Notice how I gave this place 2 stars....It's because their service is pretty much Number 2! They would not put up gutter guards for my sisters, who are not too good at bowling. They have some cranky guy running the only counter and seriously the only upside to this place is the Cosmic Bowling.", "user": "/operationrepo/api/user/8OrUcPNfWnwjFP0Z5wSRrA/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2012-11-08", "review_id": "4Ch-4JeCWsSms0AoUXIiOw", "stars": 4.0, "text": "I came here on a Saturday night to watch an ASU game and have a nice dinner. It's located right off Scottsdale Road, easily visible from the street. There was no wait when we came (around 8PM) but very packed. We were seated at a bar top and were quickly greeted by our waiter. I decided to order a raspberry margarita, which was pretty good. I do prefer margaritas on the rocks and this one was frozen. I ordered a caesar salad to start and the chicken alfredo. The alfredo pasta came with rotini noodles, which I liked but reminded me slightly of a macaroni and cheese. The portion was HUGE though, definitely share or plan to take a lot home! Everything was good, the place has a bunch of TV's and the bar area with the TV on was really loud. If you don't like to watch sports while eating/drinking, I probably wouldn't come here. But, if you don't mind it or like it, it's a fun place to check out. \n\nOverall, I had a good time and would recommend.", "user": "/operationrepo/api/user/cBJqlNzyoJFak3_XRe2bvw/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01kU7NKzfCP3tgYmgzXbjQ/", "date": "2011-03-01", "review_id": "ZYByZs1t5CiS3k51Dc7apA", "stars": 2.0, "text": "Price of water went up. \nFrozen yogurt is either vanilla or chocolate. \nSome hot food eg: nachos, hot dogs\nSmells musty. \nStaff is slow.", "user": "/operationrepo/api/user/8z2mKSqTW-4pLobAUNvrsQ/", "votes": {"cool": 0, "funny": 1, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2010-08-22", "review_id": "GmkYnZW9Q8rf9BZWoD3V_A", "stars": 4.0, "text": "With football season just around the corner, I am so happy to have Blue 32 open in my neighborhood! (Now I have no reason to ever step in Zipp's again, I definitely won't miss the smell of dirty rags and the crappy food!) \n\nI decided to check it out on Saturday for lunch, I thought that I should try to preview it before it becomes packed during football season. Blue 32 is an upscale sports bar, the inside is crisp and clean and there are TONS of flat-screen TVs all over the place! The menu is huge....so many options and many of them unique that you don't see on a regular sports bar menu. \n\nWe started with a basket of onion rings, and wow, yummy! They batter was light, but they had added a touch of heat to the batter, that made them perfect for dunking in cool, creamy ranch dressing! \n\nI ordered the Shrimp & Bacon Quesadilla off of the appetizer section, which I though was a nice change from the standard chicken quesadilla (which they do have for traditionalists). The quesadilla was huge, filled with shrimp, bacon and cheese and served with guacamole and sour cream, it was amazing and big enough that I got to bring home leftovers! \n\nMy friends tried the BBQ Chicken Flatbread and the classic BLT. They both really liked their dishes, and like the quesadilla, both portions were big and required take home boxes! \n\nThis is my new go to place, I can't wait to try out more of the menu and watch 4 football games at once!", "user": "/operationrepo/api/user/fAiVqZv7P_oc5CzGMX_G9w/", "votes": {"cool": 1, "funny": 0, "useful": 1}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2011-06-15", "review_id": "Io_AFAWeSHtyHVe3HD69-Q", "stars": 4.0, "text": "Met some friends here to watch the Boston/Vancouver game 6. Big, open modern upscale space with plenty of high-quality Panasonic 50\" TV's all over the place. This is important to me being from the audio/video business- many sports bars buy the cheapest HDTV's they can find and it really shows.\n\nGreat beer specials- \\$2.75 domestic drafts till 7pm, our group loved the fish tacos and huge chicken wings that you can order how you like (all drums please).\n\nDefinitely will be back.\n\nBOTTOM LINE: Blue 32 I'll be a regular here too.", "user": "/operationrepo/api/user/_-Zrzf2QYiw4KHugUTXNYQ/", "votes": {"cool": 0, "funny": 0, "useful": 2}}, {"business": "/operationrepo/api/business/022T8YSRmb3b1BfwzO3F7Q/", "date": "2012-03-20", "review_id": "Zuc_PEXMphLDn3mjc_nZEg", "stars": 2.0, "text": "We have been going here for several years and every time the only thing consistent is the rude staff behind the front desk.\nMy grandson was visiting from Cali for spring break and wanted to go bowling yesterday.  I am on their email list and had received a coupon for two hours of bowling with shoes, food, etc for \\$7.99.  I asked for the special rate and was very rudely told that it doesn't apply during spring break and that lanes were \\$3+ and shoes were \\$4.50.  When I asked about who has spring break now he rudely replied Paradise Valley schools.  Really????  This was Scottsdale, wtf?\nSo I paid over \\$30 for three of us to bowl.  When I asked for two lanes (one w/ bumper for grandson) he acted really put out.\nWe had a good time, but both my daughter and myself have our own shoes and I felt ripped off and hate rude workers, so I was mad.\nThen afterwords we went to the game part of the place and almost every game was broken or did not give out tickets.  My grandson wanted to play ski ball he loves and they were broken too.  Of course the desk people could care less.\nWe will not be going back here again. Too many times they have treated us like crap and I would much rather take my money somewhere else where I am appreciated and provides even some sort of customer service.", "user": "/operationrepo/api/user/eqHh3T-QWN8bowagW4KiGg/", "votes": {"cool": 0, "funny": 0, "useful": 2}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2010-08-16", "review_id": "VKWoV25wNpdNWLXzUwgUpA", "stars": 4.0, "text": "These guys have a nice place in a great location.\n\nI sat at a table in the bar and watched part of the Saturday round of the PGA.  As previous reviewers have mentioned, there are plenty of flat screens here.\n\nI ordered a grinder, fries and iced tea.  They were all very good.\n\nThe service was super friendly and I'm looking forward to coming back soon.", "user": "/operationrepo/api/user/Kqvfep2mxS10S50FbVDi4Q/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2012-06-15", "review_id": "6H5NYBjN_IiiRq2xAxbOWg", "stars": 4.0, "text": "Big sports bar with more TVs than you can count, ice (and I mean ice, frosty) cold beer, delicious food (try the mushroom swiss burger, and definitely the onion rings), and fantastic service.  What more could you ask for??  For catching any big game this is the place to be!", "user": "/operationrepo/api/user/Yoa2y89jR7tAnWRLSDca7Q/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2012-09-23", "review_id": "y1vMRm5hml7AnilMCv6ivg", "stars": 5.0, "text": "great sports bar. TV's galore. Good food. Outside patio. While many places claim to be sports bars, for some reason they wind up not paying attention to the TV's and wind up with hair removal infomercials playing.\n\nThis place knows what they are doing with the tv's. I was watching the manager who looked like had a spreadsheet with every game planned out and on what tv's. They also play the sound from the premier game.", "user": "/operationrepo/api/user/e74v9ab0-PgmiwBhdbj_XQ/", "votes": {"cool": 0, "funny": 0, "useful": 3}}, {"business": "/operationrepo/api/business/00eGk1ntf4RiDxVRY3gaIw/", "date": "2009-01-31", "review_id": "eOGI5qb_fBf1sbZxB1mu-w", "stars": 3.0, "text": "Buffalo Wings are pretty good.  i had them with the mojo ipa which is perfect with spicy food.  then we had a deep dish classic pizza.  good dough and decent cheese/topping/sauce ratio.", "user": "/operationrepo/api/user/EpC7vMp0hg1wGBQ6fzzoQg/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/022T8YSRmb3b1BfwzO3F7Q/", "date": "2013-05-13", "review_id": "SziI2G4DcMEA7TIxVYRtrQ", "stars": 2.0, "text": "Got serviced by Brad. Very disappointed with the experience because of him.", "user": "/operationrepo/api/user/0ZhANN52GKlx-u9gxN8K7Q/", "votes": {"cool": 0, "funny": 0, "useful": 0}}, {"business": "/operationrepo/api/business/01cEFI5Pq_RyEwM3GSTopQ/", "date": "2011-12-31", "review_id": "xWAvESbLyNmdpdvK32zz5g", "stars": 4.0, "text": "Good food and able to manage a large group easily. Our party had 11 and there wasn't a long wait at all. Highlights: spinach and artichoke dip, onion rings, and tortilla soup. Total tab was only \\$160 for the whole group.", "user": "/operationrepo/api/user/4Nc0DPLqeSZuqvr1gBTy3Q/", "votes": {"cool": 0, "funny": 0, "useful": 0}}]
        self.assertTrue(content==actual)

    def test_api_get_review(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/rGWvvzfxIv-aoAKGGGHrMg/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual =  {"business": "/operationrepo/api/business/022T8YSRmb3b1BfwzO3F7Q/", "date": "2011-01-12", "review_id": "rGWvvzfxIv-aoAKGGGHrMg", "stars": 4.0, "text": "Fun place! We've mostly just been here for our league's cosmic bowling nights. It's a fun place to socialize and have fun with your friends. The prices are good too!", "user": "/operationrepo/api/user/xFG4Ca2HHmbxDTkMlmHnjQ/", "votes": {"cool": 0, "funny": 0, "useful": 0}}
        self.assertTrue(content==actual)

    def test_api_get_bad_review(self):
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/nothere/")
        try :
            response = urlopen(request)
        except HTTPError :
            return True
        return False

    #api post tests
    # -----
    # post
    # -----
    def test_api_post_user(self) :
        values = "{\"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/", data=values.encode("utf-8"), headers=headers, method="POST")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_post_business(self) :
        values = "{\"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/", data=values.encode("utf-8"), headers=headers, method="POST")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_post_review(self) :
        values = "{\"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/", data=values.encode("utf-8"), headers=headers, method="POST")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 201)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_put_user(self) :
        values = "{\"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/AHzLh-2WyMjf6TYATFwg6N", data=values.encode("utf-8"), headers=headers, method="PUT")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_put_business(self) :
        values = "{\"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/AHzLh-2WyMjf6TYATFwg6N", data=values.encode("utf-8"), headers=headers, method="PUT")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_put_review(self) :
        values = "{\"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/AHzLh-2WyMjf6TYATFwg6N", data=values.encode("utf-8"), headers=headers, method="PUT")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_delete_user(self) :
        values = "{\"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/user/", data=values.encode("utf-8"), headers=headers, method="DELETE")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"user_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_delete_business(self) :
        values = "{\"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/business/", data=values.encode("utf-8"), headers=headers, method="DELETE")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"business_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")

    def test_api_delete_review(self) :
        values = "{\"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\"}"
        headers = {"Content-Type": "application-json"}
        request = Request("http://cs373-oprepo.herokuapp.com/OperationRepo/api/review/", data=values.encode("utf-8"), headers=headers, method="DELETE")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 204)

        response_body = response.read()
        self.assertTrue(response_body.decode("utf-8") == "{ \"review_id\": \"AHzLh-2WyMjf6TYATFwg6N\" }")
print ("Done")

