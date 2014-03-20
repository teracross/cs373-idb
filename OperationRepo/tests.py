from urllib.request import urlopen, Request
from json import dumps, loads
from django.test import TestCase

class API_Test(TestCase) :

	# -----
	# get all
	# -----
	def test_get_businesses(self) :
		request = Request("http://oprepo.apiary.io/api/businesses")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = [
			{
				"id": 1,
				"business_id": "O_X3PGhk3Y5JWVi866qlJg",
				"name": "Turf Paradise Race Course"
			},
			{
				"id": 2,
				"business_id": "QbrM7wqtmoNncqjc6GtFaQ",
				"name": "Sam's Club Members Only"
			}
		]
		
		self.assertTrue(content == actual)

		
	def test_get_users(self) :
		request = Request("http://oprepo.apiary.io/api/users")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = [
			{
				"id": 1,
				"user_id": "2WyMjf6TYATFwg6NA",
				"name": "Glen"
			},
			{
				"id": 2,
				"business_id": "gYV6bmTSgbZMGkvXHVCowg",
				"name": "Paul"
			}
		]
		
		self.assertTrue(content == actual)

		
	def test_get_reviews(self) :
		request = Request("http://oprepo.apiary.io/api/reviews")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = [
			{
				"id": 1,
				"user_id": "r-t7IiTSD0QZdt8lOUCqeQ",
				"review_id": "0ESSqLfOae77muWTv_zUqA",
				"business_id": "WIcDFpHEnC3ihNmS7-6-ZA"
			},
			{
				"id": 2,
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
		request = Request("http://oprepo.apiary.io/api/businesses", data=values.encode("utf-8"), headers=headers)
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

		response_body = response.read()
		self.assertTrue(response_body.decode("utf-8") == "{ id: 1 }")

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
		request = Request("http://oprepo.apiary.io/api/users", data=values.encode("utf-8"), headers=headers)
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

		response_body = response.read()
		self.assertTrue(response_body.decode("utf-8") == "{ id: 1 }")

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
		request = Request("http://oprepo.apiary.io/api/reviews", data=values.encode("utf-8"), headers=headers)
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

		response_body = response.read()
		self.assertTrue(response_body.decode("utf-8") == "{ id: 2 }")


	# -----
	# get single
	# -----		
	def test_get_businesses_single(self) :
		request = Request("http://oprepo.apiary.io/api/businesses/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = { 
			"id": 1,
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
		}
		self.assertTrue(content == actual)

		
	def test_get_users_single(self) :
		request = Request("http://oprepo.apiary.io/api/users/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = { 
			"id": 1,
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
	
		
	def test_get_reviews_single(self) :
		request = Request("http://oprepo.apiary.io/api/reviews/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = { 
    		"id": 2,
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
		request = Request("http://oprepo.apiary.io/api/businesses/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		self.assertTrue(response.getcode(), 204)


	def test_delete_user(self) : 
		request = Request("http://oprepo.apiary.io/api/users/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		self.assertTrue(response.getcode(), 204)


	def test_delete_review(self) : 
		request = Request("http://oprepo.apiary.io/api/reviews/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)

		self.assertTrue(response.getcode(), 204)


	# -----
	# get reviews for business
	# -----
	def test_get_business_reviews(self) :
		request = Request("http://oprepo.apiary.io/api/businesses/{id}/reviews")
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
	# get users who reviewed business 
	# -----
	def test_get_business_users(self) :
		request = Request("http://oprepo.apiary.io/api/businesses/{id}/users")
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
	# get businesses reviewed by user
	# -----
	def test_get_user_businesses(self) :
		request = Request("http://oprepo.apiary.io/api/users/{id}/businesses")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = [
	{
		"business_id": "KWo4geULVPzCirc0Scpcow",
		"full_address": "3701-3965 Sky Harbor Blvd\nPhoenix, AZ 85034",
		"hours": {},
		"open": True,
		"categories": ["Bakeries", "Food", "French", "Restaurants"],
		"city": "Phoenix",
		"review_count": 12,
		"name": "La Madeleine",
		"neighborhoods": [],
		"longitude": -112.001445002113,
		"state": "AZ",
		"stars": 3.5,
		"latitude": 33.433677495519298,
		"attributes": {"Wi-Fi": "free",
					"Good For": {"dessert": False,
								"latenight": False,
								"lunch": False,
								"dinner": False,
								"brunch": False,
								"breakfast": False},
					"Delivery": False,
					"Outdoor Seating": False,
					"Attire": "casual",
					"Waiter Service": False,
					"Accepts Credit Cards": True},
		"type": "business"
	}
]
		self.assertTrue(content == actual)


	# -----
	# get reviews by user
	# -----
	def test_get_user_reviews(self) :
		request = Request("http://oprepo.apiary.io/api/users/{id}/reviews")
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
		request = Request("http://oprepo.apiary.io/api/reviews/{id}/businesses")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

		body_content = response.readall().decode("utf-8")
		content = loads(body_content)
		actual = [
    {
        "business_id": "70p94Ejeu1v5XlIkbKORYQ",
        "full_address": "3479 E Baseline Rd\nSte 18\nGilbert, AZ 85234",
        "hours": {"Monday": {"close": "19:00", "open": "09:00"},
                "Tuesday": {"close": "19:00", "open": "09:00"},
                "Friday": {"close": "19:00", "open": "09:00"},
                "Wednesday": {"close": "19:00", "open": "09:00"},
                "Thursday": {"close": "19:00", "open": "09:00"},
                "Saturday": {"close": "19:00", "open": "09:00"}},
        "open": True,
        "categories": ["Hair Salons", "Beauty & Spas"],
        "city": "Gilbert",
        "review_count": 9,
        "name": "Salon Lola",
        "neighborhoods": [],
        "longitude": -111.75560249999999,
        "state": "AZ",
        "stars": 5.0,
        "latitude": 33.379065699999998,
        "attributes": {"Price Range": 2,
                    "Parking": {"garage": False,
                                "street": False,
                                "validated": False,
                                "lot": True,
                                "valet": False},
                    "By Appointment Only": True,
                    "Accepts Credit Cards": True,
                    "Good for Kids": True,
                    "Wheelchair Accessible": True},
        "type": "business"
    }
]
		self.assertTrue(content == actual)


	# -----
	# get user from review
	# -----
	def test_get_review_user(self) :
		request = Request("http://oprepo.apiary.io/api/reviews/{id}/users")
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
		request = Request("http://oprepo.apiary.io/api/businesses/{id}", data=values.encode("utf-8"), headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)


	def test_put_user(self) :
		values = "{ \n    \"yelping_since\": \"2011-08\",\n    \"votes\": {\"funny\": 0,\n            \"useful\": 1,\n            \"cool\": 1},\n    \"review_count\": 5,\n    \"name\": \"Glen\",\n    \"user_id\": \"HzLh-2WyMjf6TYATFwg6NA\",\n    \"friends\": [],\n    \"fans\": 0,\n    \"average_stars\": 3.6000000000000001,\n    \"type\": \"user\",\n    \"compliments\": {},\n    \"elite\": [],\n}"
		headers = {"Content-Type": "application-json"}
		request = Request("http://oprepo.apiary.io/api/users/{id}", data=values.encode("utf-8"), headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertTrue(response.getcode() == 204)


	def test_put_review(self) :
		values = "{ \n    \"votes\": {\"funny\": 0,\n            \"useful\": 0,\n            \"cool\": 0},\n    \"user_id\": \"SS85hfTApRnbTPcJadra8A\",\n    \"review_id\": \"VyAKIaj_Rmsf_ZCHcGJyUw\",\n    \"stars\": 5,\n    \"date\": \"2010-05-30\",\n    \"text\": \"I love Marilo!  She understands my hair type and knows exactly what to do with my hair.  She keeps a record of my previous visits.  She recommends what is best for my hair.  She is pleasant to work with: easygoing, friendly, and respectful.  I've been going to her since 2008.  I'm really picky with hair people, and I used to go back to Chicago for haircuts.  Now, I stick to Marilo.\",\n    \"type\": \"review\",\n    \"business_id\": \"70p94Ejeu1v5XlIkbKORYQ\"\n}"
		headers = {"Content-Type": "application-json"}
		request = Request("http://oprepo.apiary.io/api/reviews/{id}", data=values.encode("utf-8"), headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		response_body = response.read()
		self.assertTrue(response.getcode() == 204)

	



print ("Done")
		
