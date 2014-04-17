from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import dumps, loads
from django.test import TestCase

class SearchTest(TestCase):

    def test_search_singleword(self):
        request = Request("http://0.0.0.0:5000/operationrepo/search/?format=json&search=blah")
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)
        content = loads(response.readall().decode("utf-8"))
        #print(content)
        actual = {"andresults": ["[{\"pk\": \"sZMUjLKuxXnzgfEGDDbQow\", \"model\": \"OperationRepo.review\", \"fields\": {\"date\": \"2013-02-04\", \"text\": \"Lots of TVs and good beer selection, but the food is probably below average, even for a sports bar. I had the philly which was blah and the nachos left a lot to be desired as well. Oh, and the niners lost :-(\", \"stars\": 3.0, \"user\": \"pi_f7sm9mclhBMtRHvGL1w\", \"business\": \"01cEFI5Pq_RyEwM3GSTopQ\"}}]", "[]", "[]"], "search_terms": "blah", "orresults": ["[]", "[]", "[]"]}
        self.assertTrue(content == actual)

    def test_search_tempty(self):
        request = Request('http://0.0.0.0:5000/operationrepo/search/?format=json&search=""')
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)
        content = loads(response.readall().decode("utf-8"))
        #print(content)
        actual = {"andresults": ["[]", "[]", "[]"], "search_terms": "\"\"", "orresults": ["[]", "[]", "[]"]}
        self.assertTrue(content == actual)

    def test_search_multiple(self):
        request = Request('http://0.0.0.0:5000/operationrepo/search/?format=json&search=blah+pool')
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)
        content = loads(response.readall().decode("utf-8"))
        actual = {"andresults": ["[]", "[]", "[]"], "search_terms": "blah pool", "orresults": ["[{\"pk\": \"u2NF5830MGdwgQQo74ti0Q\", \"model\": \"OperationRepo.review\", \"fields\": {\"date\": \"2013-07-17\", \"text\": \"I haven't bowled in years. So when a group of friends put together an outing here, I had to come. We bowled on a Saturday afternoon around 1 pm and the place was wide open. They had the black lights, neon, loud music, and lasers going on...kind of weird to have cosmic bowling in the middle of the day....whatever, it was cool.\\n\\nWe paid \\\\$20 for 2 of us to play 2 games each....\\\\$5 per game. Price comes with the shoes. The selection of bowling balls is kind of limited. It took us a little while to find a ball for us to use. Bowling was fun though...very laid back and everyone had a good time.\\n\\nThe food options here are ok....Hot Dogs, Pizza, Fries....typical bowling alley food. On the plus side...they serve Nathan's Hot Dogs...so at least they're quality. The Pizza is plain though...below average.\\nhttp://www.yelp.com/biz_photos/brunswick-via-linda-lanes-scottsdale?select=W8kuwKmK0s-yqa3Z_yWD0w#W8kuwKmK0s-yqa3Z_yWD0w\\n\\nSome other notes - They also have a pool table in another room. There are lockers available to store your stuff. If you want to drink alcoholic beverages, they have a small lounge/bar...will have to check that out next time.\\n\\nOverall, it was a very good time. Since it's in the neighborhood, we'll definitely be back.\\n\\nReturn Factor - 90%\", \"stars\": 4.0, \"user\": \"kGgAARL2UmvCcTRfiscjug\", \"business\": \"022T8YSRmb3b1BfwzO3F7Q\"}}, {\"pk\": \"sZMUjLKuxXnzgfEGDDbQow\", \"model\": \"OperationRepo.review\", \"fields\": {\"date\": \"2013-02-04\", \"text\": \"Lots of TVs and good beer selection, but the food is probably below average, even for a sports bar. I had the philly which was blah and the nachos left a lot to be desired as well. Oh, and the niners lost :-(\", \"stars\": 3.0, \"user\": \"pi_f7sm9mclhBMtRHvGL1w\", \"business\": \"01cEFI5Pq_RyEwM3GSTopQ\"}}]", "[]", "[]"]}
        self.assertTrue(content == actual)

print ("Done")