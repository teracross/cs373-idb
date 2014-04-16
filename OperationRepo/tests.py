from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import dumps, loads
from django.test import TestCase

class API_Test(TestCase) :

    # base url to test API
    url = "http://cs373-oprepo.herokuapp.com/OperationRepo/api/"

    # tests against actual database

    #---
    #api get tests
    #---
    def test_api_get_all_business(self):
        request = Request(self.url + "business/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [ { "city": "Goodyear",  "business_id": "02rrDia_FTc8jN7LGqzIbQ",  "name": "Corral West Arena" },  { "city": "Phoenix",  "business_id": "02Fijjr_ccD42E-5aGOXWQ",  "name": "Pure Air Service Arizona" },  { "city": "Scottsdale",  "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "name": "Brunswick Via Linda Lanes" },  { "city": "Surprise",  "business_id": "01kU7NKzfCP3tgYmgzXbjQ",  "name": "Water Fountain" },  { "city": "Mesa",  "business_id": "01euuGhBwvcDhl9KcPTang",  "name": "El Salsita" },  { "city": "Glendale",  "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "name": "Mario's Hair Company" },  { "city": "Scottsdale",  "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "name": "Blue 32 Sports Grill" },  { "city": "Phoenix",  "business_id": "015GCpe-tMj1En4NORROzA",  "name": "Elite Cleaners" },  { "city": "Surprise",  "business_id": "00FGafv0TKfmH_QhVxh4FQ",  "name": "Tom's Camperland" },  { "city": "Mesa",  "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "name": "Old Chicago" } ]
        self.assertTrue(content==actual)

    def test_api_get_business(self):
        request = Request(self.url + "business/00eGk1ntf4RiDxVRY3gaIw/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = { "yelp_url": "http://www.yelp.com/biz/old-chicago-mesa-3",  "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "hours": { "Saturday": { "open": "11:00",  "close": "02:00" },  "Wednesday": { "open": "11:00",  "close": "02:00" },  "Thursday": { "open": "11:00",  "close": "02:00" },  "Friday": { "open": "11:00",  "close": "02:00" },  "Monday": { "open": "11:00",  "close": "02:00" },  "Tuesday": { "open": "11:00",  "close": "02:00" },  "Sunday": { "open": "11:00",  "close": "02:00" } },  "state": "AZ",  "stars": 3.0,  "categories": [ "American (Traditional)",  "Pizza",  "Salad",  "Restaurants" ],  "full_address": "6821 E Superstition SpringsMesa, AZ 85209",  "type": "business",  "city": "Mesa",  "attributes": { "good_for": { "dinner": True,  "latenight": False,  "brunch": False,  "breakfast": False,  "lunch": True,  "dessert": True },  "wheelchair_accessible": "True",  "good_for_dancing": "False",  "parking": { "valet": False,  "lot": True,  "garage": False,  "validated": False,  "street": False },  "coat_check": "False",  "good_for_groups": "True",  "ambience": { "casual": True,  "divey": False,  "classy": False,  "hipster": False,  "romantic": False,  "intimate": False,  "upscale": False,  "trendy": False,  "touristy": False },  "noise_level": "very_loud",  "outdoor_seating": "True",  "alcohol": "full_bar",  "waiter_service": "True",  "takeout": "True",  "smoking": "outdoor",  "attire": "casual",  "happy_hour": "True",  "good_for_kids": "True",  "accepts_credit_cards": "True",  "delivery": "False",  "price_range": "2",  "has_tv": "True",  "takes_reservations": "False",  "music": { "dj": False,  "jukebox": False,  "video": False,  "background_music": True,  "karaoke": False,  "live": False },  "wifi": "free" },  "is_open": True,  "longitude": -111.6837464,  "name": "Old Chicago",  "review_count": 23,  "latitude": 33.3832251 } 
        self.assertTrue(content==actual)

    def test_api_get_bad_business(self):
        request = Request(self.url + "business/nothere/")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 404)
            self.assertTrue(e.reason == "NOT FOUND")
        return False

    def test_api_get_bad_business2(self):
        request = Request(self.url + "business/ /")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 400)
            self.assertTrue(e.reason == "BAD_REQUEST")
        return False

    def test_api_get_all_users(self):
        request = Request(self.url + "user/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [ { "user_id": "x5-yK8bmjQTcMrlWLfgJEg",  "name": "lisa" },  { "user_id": "Ae_rbQ293MYrKaywJT6Oeg",  "name": "Amanda" },  { "user_id": "8EaO99Q3E_SS8KzOR1rFrA",  "name": "Brian" },  { "user_id": "EsZoGB023YUubq7rC7rm8Q",  "name": "Paul" },  { "user_id": "fdnSC-PGo2mYTgcOEq6Bpw",  "name": "Peter" },  { "user_id": "90a6z--_CUrl84aCzZyPsg",  "name": "Michael" },  { "user_id": "egm1AgWT-cttbm4nu_FVcQ",  "name": "Scooter" },  { "user_id": "eqHh3T-QWN8bowagW4KiGg",  "name": "marty" },  { "user_id": "KbmjlHxkj4dA8t90IWjgpQ",  "name": "Kris" },  { "user_id": "a8Xp9eCcmtWKhnlB5V4Ghg",  "name": "Ingrid" },  { "user_id": "NFaCr9xvyDBioc2mB1w08w",  "name": "Kate" },  { "user_id": "bZaSmDxmKbVNOOAdzxX_bg",  "name": "Erin" },  { "user_id": "wBi0I2QcqZtNOh21WlBVKA",  "name": "John" },  { "user_id": "yWBwbPCOy8eBD1wWSH6s_A",  "name": "Ricky" },  { "user_id": "Kqvfep2mxS10S50FbVDi4Q",  "name": "Patrick" },  { "user_id": "EVSAweqdsY_EWfDxqDYdDg",  "name": "Steven" },  { "user_id": "GjNyOTcibcI_XKCzeMgO2g",  "name": "Michael" },  { "user_id": "SEDFpR4oMPKqXMjbJiMGog",  "name": "Floyd" },  { "user_id": "fl6oI21uXoxVMwfR6lFanQ",  "name": "Tasia" },  { "user_id": "nbofxFWHORebBHh10OgYLA",  "name": "Christopher" },  { "user_id": "HVqnEnkir1iGG0185VzYRA",  "name": "Will" },  { "user_id": "3d6Mhk-Bx1p75jmy3AVJWA",  "name": "Drew" },  { "user_id": "LLdbxv769G-mzDYs3Njjcw",  "name": "A." },  { "user_id": "8aBoNgjAi8cn15UsoHWQFw",  "name": "Trisha" },  { "user_id": "jy1qPe0Tz3ewHacAtshmBw",  "name": "Sarah" },  { "user_id": "LdhwY7eudLlx1KFQQe9GwA",  "name": "Josh" },  { "user_id": "33vUIil_GCaT92aUaZhRXA",  "name": "Fairbi" },  { "user_id": "dVomZlKABGY3iX3ULkkQpA",  "name": "Nick" },  { "user_id": "Z9QRZYyh-xPtpM2W9euDiQ",  "name": "Jonathan" },  { "user_id": "E3Koa54vrcDs5o6NoFSEwg",  "name": "Lola" },  { "user_id": "IqJjdWMgT0HxrPP_-kWPmw",  "name": "Cory" },  { "user_id": "f5DSsK2w-b0xQVyz8lZACw",  "name": "Terry" },  { "user_id": "OqgL64SkHicaRtYpw08r9g",  "name": "Whitney" },  { "user_id": "XqMkm-DD9VsdcKx2YVGhSA",  "name": "Bao" },  { "user_id": "RdWhGfwHORbIEyFj6YbZow",  "name": "N" },  { "user_id": "-1F7KZxq3Lib1CKLlybC5Q",  "name": "Barbara" },  { "user_id": "DI1wmnA_Pg9mycZV84_syw",  "name": "Matt" },  { "user_id": "Y66q9-Nggoo6W5BgoP5FbA",  "name": "Karli" },  { "user_id": "OOxLwlNadygUwL_aG8KnSQ",  "name": "Cyn" },  { "user_id": "gSBvJ5FqFeSKRJaPiamttw",  "name": "Bradley" },  { "user_id": "cl9ZMopdCQGGXMlwgruFdg",  "name": "Diana" },  { "user_id": "CjVX1QGNqx3_oDBuRig4-A",  "name": "Sarah" },  { "user_id": "w1LjSa5wMexRIQ-82LKWmQ",  "name": "Amy" },  { "user_id": "DESuUHNcQUULDCS9KlNVcw",  "name": "Theresa" },  { "user_id": "8OrUcPNfWnwjFP0Z5wSRrA",  "name": "Varun" },  { "user_id": "b927p9pWxM9EYoNr_6PxYQ",  "name": "Andrew" },  { "user_id": "syJ-WZZ1vcbQZgtjqmJ1uA",  "name": "Deuce" },  { "user_id": "RNxfe4lnDNjbQWa2-oIdEA",  "name": "Dan" },  { "user_id": "8z2mKSqTW-4pLobAUNvrsQ",  "name": "Crystal" },  { "user_id": "aGvpUCEKjKc4bqbVDiEhlQ",  "name": "Christie" },  { "user_id": "ropG9hxhgqtT865SJ3IALA",  "name": "Marco" },  { "user_id": "iwUN95LIaEr75TZE_JC6bg",  "name": "Diego" },  { "user_id": "4iAjtohAkJvMw6fVcXR_1w",  "name": "James" },  { "user_id": "b8vpDCrjDwjXSr92JVp-PQ",  "name": "Jessica" },  { "user_id": "Lu05r9ITDh8bkCqh2zz5zw",  "name": "James" },  { "user_id": "w4suxL1zlxsihVlugZZDAQ",  "name": "Lindsey" },  { "user_id": "73crJRw-NOUKGELY3hZcSw",  "name": "Julie" },  { "user_id": "Kyc_V-2G77tRfwJsBxwZ4A",  "name": "Darlene" },  { "user_id": "X6vSWes7JpMpQ6tQNtYwmA",  "name": "M" },  { "user_id": "UPtysDF6cUDUxq2KY-6Dcg",  "name": "Matt" },  { "user_id": "67q6sdXeuVRvzgHQNNHHVQ",  "name": "Clint" },  { "user_id": "5gL4Dmm5HGX8aMxvVWoSww",  "name": "Sarah" },  { "user_id": "Sjp6EYsqzdlTvymER6wBfg",  "name": "Bil" },  { "user_id": "9JpnM-xebt0343KkGR_HKQ",  "name": "The Rue" },  { "user_id": "zzmRKNph-pBHDL2qwGv9Fw",  "name": "Matt" },  { "user_id": "ALP87SgltBLmMH5OsgVrMg",  "name": "Ryan" },  { "user_id": "PS0lCxjGNeUrKxYSdpW-Aw",  "name": "Ann Marie" },  { "user_id": "PSadYWspmOQTgDs5FMOBfQ",  "name": "Colby" },  { "user_id": "LS1CRfOX3ydk7xkkCUYgmQ",  "name": "Alex" },  { "user_id": "TYHFPPZnUxvgM9OBfoN8Kg",  "name": "Carla" },  { "user_id": "8d3AGso7vTLYxXrLrkO9aQ",  "name": "Ross" },  { "user_id": "r-t7IiTSD0QZdt8lOUCqeQ",  "name": "Jan" },  { "user_id": "QAYaGDx41V0i3RQfu_5Vlg",  "name": "Matt" },  { "user_id": "MjY15QEdD0y3TIqjKxNrBg",  "name": "Guy" },  { "user_id": "palND-kF1qpMLhkcgAnSxA",  "name": "Andrea" },  { "user_id": "CPKp--5cCh4tx118LDavXQ",  "name": "John" },  { "user_id": "8lm1AvIINFQWcRbxq5blrQ",  "name": "Marie" },  { "user_id": "fczQCSmaWF78toLEmb0Zsw",  "name": "Gabi" },  { "user_id": "8CNEh7fSbLwDuAKhLjDPKQ",  "name": "Chuck" },  { "user_id": "_-Zrzf2QYiw4KHugUTXNYQ",  "name": "Scott" },  { "user_id": "7Zrq87_FzXZ-ZSwGOmas2A",  "name": "Danny" },  { "user_id": "joIzw_aUiNvBTuGoytrH7g",  "name": "Albert" },  { "user_id": "5kIo1qYtTVQzzABCkm32xA",  "name": "Gabe" },  { "user_id": "LpBWKKSNS7QmSCHppitSbg",  "name": "Joe" },  { "user_id": "IKq14A6anAGX47Gp1bsxjA",  "name": "Katie" },  { "user_id": "UquA6GumjoYaJTELY1niIg",  "name": "Eric" },  { "user_id": "-xPKyCJiK9q1OFZ7GCZwBw",  "name": "Amy" },  { "user_id": "4YreLEqgAJrg3dgPtKLuQw",  "name": "Roseanne" },  { "user_id": "8P7ikCyk2ipbiE9Ty7Bjgw",  "name": "Melanie" },  { "user_id": "tVKdmJFkmARVoVEG_pX-Qw",  "name": "Wendy" },  { "user_id": "NvDR3SPVPXrDB_dbKuGoWA",  "name": "Scott" },  { "user_id": "p7VKdqjT3WNvL7dRNNetcw",  "name": "Shirley" },  { "user_id": "Zg2LR5D8jFmdy3GQJnz8vg",  "name": "Laurence" },  { "user_id": "cBJqlNzyoJFak3_XRe2bvw",  "name": "Lauren" },  { "user_id": "EpC7vMp0hg1wGBQ6fzzoQg",  "name": "bret" },  { "user_id": "ZGW2QM4hEFgPsPzcUuBiCg",  "name": "Jake" },  { "user_id": "0ZhANN52GKlx-u9gxN8K7Q",  "name": "Andrea" },  { "user_id": "rTT04qkMm97X6Aze7uBaEg",  "name": "Lori" },  { "user_id": "DrWLhrK8WMZf7Jb-Oqc7ww",  "name": "Brad" },  { "user_id": "ocLuGkq24yjX01LVEE90sQ",  "name": "Neil" },  { "user_id": "xFG4Ca2HHmbxDTkMlmHnjQ",  "name": "Lauren" },  { "user_id": "dUQ4_JCHtqBRAs8sJUo-IA",  "name": "Hugh" },  { "user_id": "OQPPH3MMG7paqfw1THYGsQ",  "name": "Alex" },  { "user_id": "du6KeE54IFbPiXpU3LOd1g",  "name": "Donald" },  { "user_id": "yXa1HFUJ3BtSqkDwTHdAUQ",  "name": "Chad" },  { "user_id": "bPWCuFEaVL5F6dT3JgivLw",  "name": "David" },  { "user_id": "fAiVqZv7P_oc5CzGMX_G9w",  "name": "Jenn" },  { "user_id": "TQ5eVGOFr_qB5_BbEd3Sow",  "name": "MaryLou" },  { "user_id": "d_q279uWxKs9dGGV7_BjcA",  "name": "Nicholette" },  { "user_id": "4M3j1m_vlCN5BRZsDUlzyw",  "name": "Allison" },  { "user_id": "lO1iFok_4Fv_rFfRAWyhkw",  "name": "Lindsy" },  { "user_id": "J1LCKLHsNE4Cqai7WDS5kQ",  "name": "Patrick" },  { "user_id": "VWEMs0Wo98qFLl6t440PhQ",  "name": "Elyssa" },  { "user_id": "2UgCUdRuZ0bYgXAQrHpDpA",  "name": "Nina" },  { "user_id": "w_hcSjqLeSZQL9Rx1UP-Tw",  "name": "Fred" },  { "user_id": "tFyQbNbBQEyEc9oCr1pJUg",  "name": "Tyler" },  { "user_id": "UxqUq_Gq9XfPXbdzUcVhng",  "name": "Juan" },  { "user_id": "B8HTR0tC1NFe4yAuUV3tGw",  "name": "Ricky" },  { "user_id": "gJEdPm1B_gec_aHBuguJkQ",  "name": "Lauren" },  { "user_id": "icf8Tr75xv-QOnI7wZX9Xw",  "name": "Gene" },  { "user_id": "w1b0up5haKq7yOE2lv6rJA",  "name": "Drea" },  { "user_id": "DT_5ucHfprLoh78wgzY7zw",  "name": "SC" },  { "user_id": "pi_f7sm9mclhBMtRHvGL1w",  "name": "Michael" },  { "user_id": "QYgcusG-G0bwUOt0b5rT6w",  "name": "Diana" },  { "user_id": "mE2ll6yfwUvy-W7To3E0AQ",  "name": "Heather" },  { "user_id": "4Nc0DPLqeSZuqvr1gBTy3Q",  "name": "Chris" },  { "user_id": "caELu3OqZm8LkdikpmEB4w",  "name": "Phil" },  { "user_id": "ykTUd9nIYDkQYhpntgcTVw",  "name": "Joan" },  { "user_id": "GZl2QtLSCS70ocIsCbNfcQ",  "name": "Ryan" },  { "user_id": "vArhfZStEAv8is9SM_YOOQ",  "name": "M" },  { "user_id": "rO3WEI9L-_deUR9-JHuNQw",  "name": "Sarah" },  { "user_id": "f32c9cudFdr9qNhyB4ZUTw",  "name": "Kirsten" },  { "user_id": "LeU-A7akKpmPJZuXXmfdqQ",  "name": "JJ" },  { "user_id": "Sw-dAGBjXkpH2zbCRUNytw",  "name": "Paul" },  { "user_id": "yfVTtxbdnlqcWA2jXNjj_Q",  "name": "Pablo" },  { "user_id": "Uo5f4qhP0122j71IcJ1EOg",  "name": "Wheeler" },  { "user_id": "4WyOI4x62W2EsvZO-RV-MQ",  "name": "Phil" },  { "user_id": "ZZpXfbQn0nU22OGDW15TRA",  "name": "Red" },  { "user_id": "Tv9RMLng5zRcS7aFe2fAoA",  "name": "Terry" },  { "user_id": "8otDLb5-bv3ZEH0LWj1u8w",  "name": "Brian" },  { "user_id": "drS3ZN6-zA3sr5WM2fG5tQ",  "name": "Dana" },  { "user_id": "7UAhPt9AT7M3zCBF_8UInw",  "name": "Linda" },  { "user_id": "Syc4pbEkL3bbzjO4X4HhQw",  "name": "Sarah" },  { "user_id": "St8bDCbyyftkKVhXUssPJg",  "name": "Evan" },  { "user_id": "3XsGD0zJDuSQ4lvsQeTxWQ",  "name": "L" },  { "user_id": "BNZG_2nlf8hJn63FicF8Ug",  "name": "Mark" },  { "user_id": "6khNhFYFO3KSnRAM_9YdQw",  "name": "Tabitha" },  { "user_id": "o7NLSPKYo-TCCD2OtqLc2A",  "name": "Michele" },  { "user_id": "EbAgR_Lmwr6-kut0bRhV-g",  "name": "Mara" },  { "user_id": "hbRZTWNlRAVbQpImTC_0wQ",  "name": "Tyler" },  { "user_id": "Yoa2y89jR7tAnWRLSDca7Q",  "name": "Andrew" },  { "user_id": "NFZLYA8V7jIVTev_qJW1ew",  "name": "Katherine" },  { "user_id": "EemOQfYk1UL3W3GmVZADFw",  "name": "Trisha" },  { "user_id": "4ozupHULqGyO42s3zNUzOQ",  "name": "Lindsey" },  { "user_id": "zs9EphhkXylrxHCzxhC_ag",  "name": "Jarratt" },  { "user_id": "v6rb-4YhADpuD99f3RKmgg",  "name": "Marc" },  { "user_id": "kGgAARL2UmvCcTRfiscjug",  "name": "J" },  { "user_id": "NWEKM2JBpPCtvGtIsRAgMw",  "name": "Chloe" },  { "user_id": "e74v9ab0-PgmiwBhdbj_XQ",  "name": "D" },  { "user_id": "hJBOxmNREXmMGTfXgMcGug",  "name": "Derek" },  { "user_id": "qCLYzhd0L_P1iSjZJN0ZLQ",  "name": "Victor" },  { "user_id": "hckr9Hf8BUHcXfOSDv9eJA",  "name": "David" },  { "user_id": "SUcoN2gzxMX3IPfBWp-cSQ",  "name": "Tanveer" },  { "user_id": "kUKH7Mbah6TVgV_9LEnH0g",  "name": "J Ann" } ]
        self.assertTrue(content==actual)

    def test_api_get_user(self):
        request = Request(self.url + "user/x5-yK8bmjQTcMrlWLfgJEg/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = { "votes": { "useful": 4,  "cool": 1,  "funny": 3 },  "yelping_since": "2007-10-01",  "average_stars": 3.17,  "elite": [],  "fans": 0,  "user_id": "x5-yK8bmjQTcMrlWLfgJEg",  "name": "lisa",  "review_count": 8,  "type": "user",  "compliments": {} }
        self.assertTrue(content==actual)

    def test_api_get_bad_user(self):
        request = Request(self.url + "user/nothere/")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 404)
            self.assertTrue(e.reason == "NOT FOUND")
        return False

    def test_api_get_bad_user2(self):
        request = Request(self.url + "user/ /")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 400)
            self.assertTrue(e.reason == "BAD_REQUEST")
        return False

    def test_api_get_all_reviews(self):
        request = Request(self.url + "review/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = [ { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "xFG4Ca2HHmbxDTkMlmHnjQ",  "review_id": "rGWvvzfxIv-aoAKGGGHrMg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "icf8Tr75xv-QOnI7wZX9Xw",  "review_id": "UenRro_ZUAW7vmbS9Hoqrg" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "EbAgR_Lmwr6-kut0bRhV-g",  "review_id": "3fhIpynSC-C5NVEjZO-QYg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "CjVX1QGNqx3_oDBuRig4-A",  "review_id": "LcEP4Jc8ajplPSdHfiP50A" },  { "business_id": "01euuGhBwvcDhl9KcPTang",  "user_id": "vArhfZStEAv8is9SM_YOOQ",  "review_id": "_VBQ9imkoKh0dsEiDUj8tA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "kGgAARL2UmvCcTRfiscjug",  "review_id": "rPp8OWlpQX08pmaHGjsxKw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "90a6z--_CUrl84aCzZyPsg",  "review_id": "WSEPR6x1xmdst6pe8imQ7g" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "cl9ZMopdCQGGXMlwgruFdg",  "review_id": "bmOg5OJg4EMdTa2voSKEBg" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "8OrUcPNfWnwjFP0Z5wSRrA",  "review_id": "Nhxu5YD1O3NbQ00fmioKWg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "cBJqlNzyoJFak3_XRe2bvw",  "review_id": "4Ch-4JeCWsSms0AoUXIiOw" },  { "business_id": "01kU7NKzfCP3tgYmgzXbjQ",  "user_id": "8z2mKSqTW-4pLobAUNvrsQ",  "review_id": "ZYByZs1t5CiS3k51Dc7apA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "fAiVqZv7P_oc5CzGMX_G9w",  "review_id": "GmkYnZW9Q8rf9BZWoD3V_A" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "_-Zrzf2QYiw4KHugUTXNYQ",  "review_id": "Io_AFAWeSHtyHVe3HD69-Q" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "eqHh3T-QWN8bowagW4KiGg",  "review_id": "Zuc_PEXMphLDn3mjc_nZEg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Kqvfep2mxS10S50FbVDi4Q",  "review_id": "VKWoV25wNpdNWLXzUwgUpA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Yoa2y89jR7tAnWRLSDca7Q",  "review_id": "6H5NYBjN_IiiRq2xAxbOWg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "e74v9ab0-PgmiwBhdbj_XQ",  "review_id": "y1vMRm5hml7AnilMCv6ivg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "EpC7vMp0hg1wGBQ6fzzoQg",  "review_id": "eOGI5qb_fBf1sbZxB1mu-w" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "0ZhANN52GKlx-u9gxN8K7Q",  "review_id": "SziI2G4DcMEA7TIxVYRtrQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "4Nc0DPLqeSZuqvr1gBTy3Q",  "review_id": "xWAvESbLyNmdpdvK32zz5g" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "icf8Tr75xv-QOnI7wZX9Xw",  "review_id": "AaCOibzNjcJFO390GcfD1A" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "UxqUq_Gq9XfPXbdzUcVhng",  "review_id": "IG2CInbE0snsx690yKahsQ" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "dVomZlKABGY3iX3ULkkQpA",  "review_id": "915iB3PrBesqopvLj5aVJw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "fdnSC-PGo2mYTgcOEq6Bpw",  "review_id": "GjdzF2h0oN7wcMGeDmrwNA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Y66q9-Nggoo6W5BgoP5FbA",  "review_id": "xkXwxdz-sy6-33RgNoYwtg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "fl6oI21uXoxVMwfR6lFanQ",  "review_id": "7NgHS_RBr9jt_OqexRINag" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "3d6Mhk-Bx1p75jmy3AVJWA",  "review_id": "gmuri_8LSyqdMBByN-4hFA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "MjY15QEdD0y3TIqjKxNrBg",  "review_id": "rXBH7bdWh-y_Bui4DPwXDg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "drS3ZN6-zA3sr5WM2fG5tQ",  "review_id": "kJjnyz33CuMjD-XJFKzjLA" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "hbRZTWNlRAVbQpImTC_0wQ",  "review_id": "jUn0Hbwnb793MkIRE-B8aw" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "9JpnM-xebt0343KkGR_HKQ",  "review_id": "HsSOBodtfPIWnla94VxHqg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Uo5f4qhP0122j71IcJ1EOg",  "review_id": "OvNvLfzrsnHHYnt1mKdiXA" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "8EaO99Q3E_SS8KzOR1rFrA",  "review_id": "5oZjdpzWeHUSborcAmMX_Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "ALP87SgltBLmMH5OsgVrMg",  "review_id": "77kPd412-N1RZRdz3CDDTA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Sw-dAGBjXkpH2zbCRUNytw",  "review_id": "xTieoOg2q6xMN10L1JFJ-Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "gJEdPm1B_gec_aHBuguJkQ",  "review_id": "X8qTDQQ6knx-AlXTMiiqRA" },  { "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "user_id": "a8Xp9eCcmtWKhnlB5V4Ghg",  "review_id": "JEXQ7rvQkVzPNG-i9H-mUg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "w4suxL1zlxsihVlugZZDAQ",  "review_id": "cPoLz2KNAgIZ1Y7n6ebI5Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "DrWLhrK8WMZf7Jb-Oqc7ww",  "review_id": "7HiR1HaktPUP5-GhPM2_0w" },  { "business_id": "01euuGhBwvcDhl9KcPTang",  "user_id": "ropG9hxhgqtT865SJ3IALA",  "review_id": "5PMeBQmYOrK_4WQZNumM6A" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "yfVTtxbdnlqcWA2jXNjj_Q",  "review_id": "B4QL7BJp0ymzVg00k5d0mQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "NvDR3SPVPXrDB_dbKuGoWA",  "review_id": "cQwOq-mBrwyHd0H1zp1jPg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "w4suxL1zlxsihVlugZZDAQ",  "review_id": "-Mvy8Ks9NPH-QV04V0H94g" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "rTT04qkMm97X6Aze7uBaEg",  "review_id": "P5scCbOjZO2LWlbfS3ACSg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "4M3j1m_vlCN5BRZsDUlzyw",  "review_id": "Ar0NpGVlipRwkvLvkSoL1A" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "33vUIil_GCaT92aUaZhRXA",  "review_id": "a7mgWk7cgTgycY8fcCb0RQ" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "6khNhFYFO3KSnRAM_9YdQw",  "review_id": "PbuDkUXeEAhtTIANrld58A" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "4ozupHULqGyO42s3zNUzOQ",  "review_id": "mdk4rg48GxZZLAH_H9gnBg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "bZaSmDxmKbVNOOAdzxX_bg",  "review_id": "PZKssqIzCkF3fHc29MaRBg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "mE2ll6yfwUvy-W7To3E0AQ",  "review_id": "Prb-DF36Fi3T4WE6a6VT8w" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "palND-kF1qpMLhkcgAnSxA",  "review_id": "xqrumFoO1WaDVoisauqokA" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "TYHFPPZnUxvgM9OBfoN8Kg",  "review_id": "5qQ3cAUChavXkU2-2c0Zqw" },  { "business_id": "02rrDia_FTc8jN7LGqzIbQ",  "user_id": "f32c9cudFdr9qNhyB4ZUTw",  "review_id": "MXqncDc4mtqJvzvdNMMeAg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "BNZG_2nlf8hJn63FicF8Ug",  "review_id": "3NFiEmlEeq3auZL_5jE8aA" },  { "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "user_id": "joIzw_aUiNvBTuGoytrH7g",  "review_id": "bb0aYS-bSz8dkDGvOJ87Yg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "Syc4pbEkL3bbzjO4X4HhQw",  "review_id": "11v21s_RbE_b5Fg4GY0pZg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "LpBWKKSNS7QmSCHppitSbg",  "review_id": "N8e1lM3PpMXda8NCwDjXXg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "IKq14A6anAGX47Gp1bsxjA",  "review_id": "qKtePERw-WTTLdmjeqsxFg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "yXa1HFUJ3BtSqkDwTHdAUQ",  "review_id": "YyZjfu1p1fmMzc98-zfRoA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "w1b0up5haKq7yOE2lv6rJA",  "review_id": "h1GbFx-L5doQQGgQfVAVBA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "NWEKM2JBpPCtvGtIsRAgMw",  "review_id": "PPddOO15yP97VCm2BaxTsA" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "73crJRw-NOUKGELY3hZcSw",  "review_id": "vCmp8YMWcu_2733scNEsWw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "SUcoN2gzxMX3IPfBWp-cSQ",  "review_id": "dFphPvqgmZ_I-ldW1evaUA" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "d_q279uWxKs9dGGV7_BjcA",  "review_id": "x3PrP8aFCHx_0M1Ux9hIMw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "tFyQbNbBQEyEc9oCr1pJUg",  "review_id": "pUYrlcMdhJl-c7MfuW5nNA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "4WyOI4x62W2EsvZO-RV-MQ",  "review_id": "9r7_Gig9MlOesi9upn3_iw" },  { "business_id": "02Fijjr_ccD42E-5aGOXWQ",  "user_id": "NFaCr9xvyDBioc2mB1w08w",  "review_id": "WdPfWC7KrYR2O6mqEtTmzQ" },  { "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "user_id": "EVSAweqdsY_EWfDxqDYdDg",  "review_id": "8WFqRBUsKteXRTQuF6HMnQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "ykTUd9nIYDkQYhpntgcTVw",  "review_id": "jezLTk8M9APeK6xSLFjtuQ" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "w1LjSa5wMexRIQ-82LKWmQ",  "review_id": "a07rFWrQOq1aCCiYmIi4ow" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "J1LCKLHsNE4Cqai7WDS5kQ",  "review_id": "3qb9v5y6Bk-qQwUf_aM30Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "caELu3OqZm8LkdikpmEB4w",  "review_id": "Hx_IKhMODEokUcxf0YlCDA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "VWEMs0Wo98qFLl6t440PhQ",  "review_id": "6R1QXcOg4hV_-iBktVzwoQ" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "QYgcusG-G0bwUOt0b5rT6w",  "review_id": "RcN9r2S9FuGFoY7VmqksAA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "lO1iFok_4Fv_rFfRAWyhkw",  "review_id": "8-82pTh14s49IGO2L-h4kQ" },  { "business_id": "00FGafv0TKfmH_QhVxh4FQ",  "user_id": "QAYaGDx41V0i3RQfu_5Vlg",  "review_id": "xkhgcsgWTWJtDqq_gmTTZQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Ae_rbQ293MYrKaywJT6Oeg",  "review_id": "iWS1WakFB3hSepiItIUmhg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "du6KeE54IFbPiXpU3LOd1g",  "review_id": "RJS350XdAgbbF1BO3gFygA" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "7Zrq87_FzXZ-ZSwGOmas2A",  "review_id": "r5-ua0khSlgRAWYv1vhrwA" },  { "business_id": "02rrDia_FTc8jN7LGqzIbQ",  "user_id": "RNxfe4lnDNjbQWa2-oIdEA",  "review_id": "oo-KXq7dLHbEn8HrUmq7ow" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "LdhwY7eudLlx1KFQQe9GwA",  "review_id": "5iyjPz267lZgq-2F--V4-g" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "OOxLwlNadygUwL_aG8KnSQ",  "review_id": "3Y8leeubNc1pCWZJwXvsTw" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "b8vpDCrjDwjXSr92JVp-PQ",  "review_id": "1Y5jHFT6Xu9BI4JMfwdfVQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "bPWCuFEaVL5F6dT3JgivLw",  "review_id": "FSfYvhvWTRxWkzMGIMGpyw" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "DESuUHNcQUULDCS9KlNVcw",  "review_id": "XeQQoUGicvPymSmxMWQ9dw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "v6rb-4YhADpuD99f3RKmgg",  "review_id": "kVVL5yzqJH8NA8gWYvwgvg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "Kyc_V-2G77tRfwJsBxwZ4A",  "review_id": "3HUIq9kO1qYOyJdMI3VEvw" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "syJ-WZZ1vcbQZgtjqmJ1uA",  "review_id": "ccrpnUwF3WnBv2dxGHXqcg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "UPtysDF6cUDUxq2KY-6Dcg",  "review_id": "1NHba9hGNq2NRh-GGyXiZg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "2UgCUdRuZ0bYgXAQrHpDpA",  "review_id": "bENjzPqNOyOOmRQJza0dgw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "IqJjdWMgT0HxrPP_-kWPmw",  "review_id": "b9o_dVOlVeZlMoEBYkay1g" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "jy1qPe0Tz3ewHacAtshmBw",  "review_id": "xmkqZgfMbQtjmKykzlr9Rg" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "PS0lCxjGNeUrKxYSdpW-Aw",  "review_id": "9SgKmQD97UuWbXwchtT8cA" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "kGgAARL2UmvCcTRfiscjug",  "review_id": "u2NF5830MGdwgQQo74ti0Q" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "8CNEh7fSbLwDuAKhLjDPKQ",  "review_id": "GcqutPohaLV84mJniadloA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "qCLYzhd0L_P1iSjZJN0ZLQ",  "review_id": "o1OUDrBnGfXuePz3xMCf9Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "GZl2QtLSCS70ocIsCbNfcQ",  "review_id": "inEq3Q-U-SDXQQUVk7mYqA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "-xPKyCJiK9q1OFZ7GCZwBw",  "review_id": "N1xBOH3r6-1X55evn7HQ-Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "EsZoGB023YUubq7rC7rm8Q",  "review_id": "kcAq576gPEm3jglIMgZ53g" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "DT_5ucHfprLoh78wgzY7zw",  "review_id": "zBbI95K3ZEZKI0O4EVs1zA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "LeU-A7akKpmPJZuXXmfdqQ",  "review_id": "wUlYVQqedDVxAhYVByAABg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "4iAjtohAkJvMw6fVcXR_1w",  "review_id": "cQUcFUdJZwQGLKqEUhID-A" },  { "business_id": "01euuGhBwvcDhl9KcPTang",  "user_id": "TQ5eVGOFr_qB5_BbEd3Sow",  "review_id": "WvvOhGbPF9LAumTXmVSw2w" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "NFZLYA8V7jIVTev_qJW1ew",  "review_id": "r3sX7t5L4d-j-VmBHVxAnQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "OqgL64SkHicaRtYpw08r9g",  "review_id": "4LTSvtEIUFH_a1MHFJ0ekw" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "DI1wmnA_Pg9mycZV84_syw",  "review_id": "k88Z4z4EoWczNm2nLdC2Lg" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "8P7ikCyk2ipbiE9Ty7Bjgw",  "review_id": "0f0TmR2FlfJRteY7_ja0Yw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "kGgAARL2UmvCcTRfiscjug",  "review_id": "mKeU-8MNiCU6ELuviVyk7Q" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "St8bDCbyyftkKVhXUssPJg",  "review_id": "yaCGEGcI1jAtj-lsy23Ckg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "rO3WEI9L-_deUR9-JHuNQw",  "review_id": "XtgTrCTsktB8V0HpzQqI0w" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "OQPPH3MMG7paqfw1THYGsQ",  "review_id": "eAQlWAz2VRAi_hG-DEXn1g" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Sjp6EYsqzdlTvymER6wBfg",  "review_id": "kbNTTb77cdj-0FbvVcOBRg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "o7NLSPKYo-TCCD2OtqLc2A",  "review_id": "m5oSBFgl17qKFBhnGR-kOw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "hJBOxmNREXmMGTfXgMcGug",  "review_id": "_VfzqglaYhnNAgj4ycQczw" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "hckr9Hf8BUHcXfOSDv9eJA",  "review_id": "TDMTnedCuDWfd-pBIesg5w" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "b927p9pWxM9EYoNr_6PxYQ",  "review_id": "5Mm0vndA22WmlcQDpyl16g" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "gSBvJ5FqFeSKRJaPiamttw",  "review_id": "voctzxHkFjCsBmalhZWIsg" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "PSadYWspmOQTgDs5FMOBfQ",  "review_id": "EiUqNFEF6qTYBrnwMW2Olw" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "Lu05r9ITDh8bkCqh2zz5zw",  "review_id": "ncXK-yAHddX5aOWDtwqq5g" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "8lm1AvIINFQWcRbxq5blrQ",  "review_id": "nSCfHf8pB2-ypKpeDC5TRA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "f5DSsK2w-b0xQVyz8lZACw",  "review_id": "o-WYwSaJsDlLiY5PRiV9Vg" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "x5-yK8bmjQTcMrlWLfgJEg",  "review_id": "pndwlFbXLejg5HbE_IX1Qw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "8aBoNgjAi8cn15UsoHWQFw",  "review_id": "PTmGUdGB3uFhqyfAWFQjwA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "67q6sdXeuVRvzgHQNNHHVQ",  "review_id": "EbaMqCZZA0II0BoRKTR3UQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "wBi0I2QcqZtNOh21WlBVKA",  "review_id": "NVO3LXK0ViZ8ykOSiZWZtw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "RdWhGfwHORbIEyFj6YbZow",  "review_id": "hopulvB3krQQirExRfpuCg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "X6vSWes7JpMpQ6tQNtYwmA",  "review_id": "WtqJz_Awc5-oU345bolrEw" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "ZZpXfbQn0nU22OGDW15TRA",  "review_id": "UHOWw8ypHoFOwsTp86bSLg" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "E3Koa54vrcDs5o6NoFSEwg",  "review_id": "u2JZBYvXsaQiRYUNQ7X_6w" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "r-t7IiTSD0QZdt8lOUCqeQ",  "review_id": "jI14f-NzSaf5Rf3cGUgaHg" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "B8HTR0tC1NFe4yAuUV3tGw",  "review_id": "ogGpPRsAGg3KW_c47dS04A" },  { "business_id": "01kU7NKzfCP3tgYmgzXbjQ",  "user_id": "-1F7KZxq3Lib1CKLlybC5Q",  "review_id": "gRrG53-jMO8m0ZeYh3mMpA" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "zs9EphhkXylrxHCzxhC_ag",  "review_id": "IUe-42SCjoO4P49yIwPLyA" },  { "business_id": "02rrDia_FTc8jN7LGqzIbQ",  "user_id": "3XsGD0zJDuSQ4lvsQeTxWQ",  "review_id": "xZrZAqXu8DODC_t3l8QBdA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "UquA6GumjoYaJTELY1niIg",  "review_id": "mBat3LENcuf2YMKsmYl-Pw" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "Z9QRZYyh-xPtpM2W9euDiQ",  "review_id": "1QLhcHXLyeh6AOnAFpgKSQ" },  { "business_id": "02Fijjr_ccD42E-5aGOXWQ",  "user_id": "LLdbxv769G-mzDYs3Njjcw",  "review_id": "q_JF8pVHEimRzVxjkrWIWQ" },  { "business_id": "01kU7NKzfCP3tgYmgzXbjQ",  "user_id": "SEDFpR4oMPKqXMjbJiMGog",  "review_id": "H4HYAYx4_-acHc1Hz9aBPA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "E3Koa54vrcDs5o6NoFSEwg",  "review_id": "buWaZy82d33iPbahsoZAGA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "KbmjlHxkj4dA8t90IWjgpQ",  "review_id": "5I52C6pzq59Yzj_bDde_Dw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "aGvpUCEKjKc4bqbVDiEhlQ",  "review_id": "MOZDvsYt4ydT6gy4svMVsA" },  { "business_id": "00FGafv0TKfmH_QhVxh4FQ",  "user_id": "LS1CRfOX3ydk7xkkCUYgmQ",  "review_id": "JRRADUxxp7S3iVuogXQwdg" },  { "business_id": "02Fijjr_ccD42E-5aGOXWQ",  "user_id": "ocLuGkq24yjX01LVEE90sQ",  "review_id": "3BmQffTk8O3Zvzuv_hUISQ" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "4ozupHULqGyO42s3zNUzOQ",  "review_id": "jmuHKO8sWu8KSR5vwdIccg" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "ZGW2QM4hEFgPsPzcUuBiCg",  "review_id": "aoOG4BxL1cM5vm5fwtpbqQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "p7VKdqjT3WNvL7dRNNetcw",  "review_id": "MeUl2-uHuvWu2q9_njrmcw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "iwUN95LIaEr75TZE_JC6bg",  "review_id": "4taqMH-iO7JOqp6BEFGC4g" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "8otDLb5-bv3ZEH0LWj1u8w",  "review_id": "8vIoEvd21wEZXKgUvPxV5w" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "yWBwbPCOy8eBD1wWSH6s_A",  "review_id": "eLsmNIfoTU51IyH_yiAiHA" },  { "business_id": "01euuGhBwvcDhl9KcPTang",  "user_id": "nbofxFWHORebBHh10OgYLA",  "review_id": "300c4z25RYJmbTq-gqVFrA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "pi_f7sm9mclhBMtRHvGL1w",  "review_id": "sZMUjLKuxXnzgfEGDDbQow" },  { "business_id": "02Fijjr_ccD42E-5aGOXWQ",  "user_id": "egm1AgWT-cttbm4nu_FVcQ",  "review_id": "gYGsJ_hU0SxisA45THHXQw" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "zzmRKNph-pBHDL2qwGv9Fw",  "review_id": "zl1WJNgcoK7DjqPFSyhyEA" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "5kIo1qYtTVQzzABCkm32xA",  "review_id": "zqMLKzUgq_VEBT0vSoNiHQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "EemOQfYk1UL3W3GmVZADFw",  "review_id": "Od9hE-Mt2pks1upSsw8SlA" },  { "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "user_id": "Zg2LR5D8jFmdy3GQJnz8vg",  "review_id": "jeRaTLs8mF3txiFDsUPbSQ" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "DESuUHNcQUULDCS9KlNVcw",  "review_id": "5w7zQ-Ek5S2FbNnzpnj85g" },  { "business_id": "01cQQpeEwWpzTgv6YUQhAQ",  "user_id": "7UAhPt9AT7M3zCBF_8UInw",  "review_id": "6RqL_mDur6trj7mRSUijwQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "GjNyOTcibcI_XKCzeMgO2g",  "review_id": "HSa0SMZB_Jd_DrBTExwjhQ" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "90a6z--_CUrl84aCzZyPsg",  "review_id": "7OwjuLOgs_WdBvJyg4glsw" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "XqMkm-DD9VsdcKx2YVGhSA",  "review_id": "YxZL_AJUWp7ejS_S4gNn1A" },  { "business_id": "00eGk1ntf4RiDxVRY3gaIw",  "user_id": "tVKdmJFkmARVoVEG_pX-Qw",  "review_id": "aRYsv5K7R6MMrTVGKJLXEQ" },  { "business_id": "00FGafv0TKfmH_QhVxh4FQ",  "user_id": "kUKH7Mbah6TVgV_9LEnH0g",  "review_id": "E3qstWP4nnj9Xrfzd8K51A" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "fczQCSmaWF78toLEmb0Zsw",  "review_id": "Ns-Rnd5mNAFRm2C2DHMpnQ" },  { "business_id": "015GCpe-tMj1En4NORROzA",  "user_id": "5gL4Dmm5HGX8aMxvVWoSww",  "review_id": "tl86EaBeiHV98VgnLG3wBQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "CPKp--5cCh4tx118LDavXQ",  "review_id": "SpiaXtkFogAVFbepNovdTQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "w_hcSjqLeSZQL9Rx1UP-Tw",  "review_id": "72qnAssI-1kWh-2AIbcNew" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "Tv9RMLng5zRcS7aFe2fAoA",  "review_id": "ufaAc5lqzPAirWN3SnylMA" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "8d3AGso7vTLYxXrLrkO9aQ",  "review_id": "4cTnfiJuNtLxzTRrJhcRdQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "dUQ4_JCHtqBRAs8sJUo-IA",  "review_id": "T4bnSU_hb0hQmtzB-uPivQ" },  { "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "user_id": "HVqnEnkir1iGG0185VzYRA",  "review_id": "wW92ebtfbllo0dmBMf_qOQ" },  { "business_id": "01cEFI5Pq_RyEwM3GSTopQ",  "user_id": "4YreLEqgAJrg3dgPtKLuQw",  "review_id": "vm3Xh6hYzcCZQtyEUeWPhA" } ]
        self.assertTrue(content==actual)

    def test_api_get_review(self):
        request = Request(self.url + "review/rGWvvzfxIv-aoAKGGGHrMg/")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)

        body_content = response.readall().decode("utf-8")
        content = loads(body_content)
        actual = { "votes": { "useful": 0,  "cool": 0,  "funny": 0 },  "business_id": "022T8YSRmb3b1BfwzO3F7Q",  "text": "Fun place! We've mostly just been here for our league's cosmic bowling nights. It's a fun place to socialize and have fun with your friends. The prices are good too!",  "review_id": "rGWvvzfxIv-aoAKGGGHrMg",  "type": "review",  "user_id": "xFG4Ca2HHmbxDTkMlmHnjQ",  "date": "2011-01-12",  "stars": 4.0 }
        self.assertTrue(content==actual)

    def test_api_get_bad_review(self):
        request = Request(self.url + "review/nothere/")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 404)
            self.assertTrue(e.reason == "NOT FOUND")
        return False

    def test_api_get_bad_review2(self):
        request = Request(self.url + "review/ /")
        try :
            response = urlopen(request)
        except HTTPError as e:
            self.assertTrue(e.code == 400)
            self.assertTrue(e.reason == "BAD_REQUEST")
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
        print (reponse.read().decode("utf-8"))
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

