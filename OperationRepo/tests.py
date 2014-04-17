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
        request = Request('http://0.0.0.0:5000/operationrepo/search/?format=json&search=blah+welcome')
        response = urlopen(request)
        self.assertEqual(response.getcode(), 200)
        content = loads(response.readall().decode("utf-8"))
        actual = {"andresults": ["[]", "[]", "[]"], "search_terms": "blah welcome", "orresults": ["[{\"pk\": \"sZMUjLKuxXnzgfEGDDbQow\", \"model\": \"OperationRepo.review\", \"fields\": {\"date\": \"2013-02-04\", \"text\": \"Lots of TVs and good beer selection, but the food is probably below average, even for a sports bar. I had the philly which was blah and the nachos left a lot to be desired as well. Oh, and the niners lost :-(\", \"stars\": 3.0, \"user\": \"pi_f7sm9mclhBMtRHvGL1w\", \"business\": \"01cEFI5Pq_RyEwM3GSTopQ\"}}, {\"pk\": \"YxZL_AJUWp7ejS_S4gNn1A\", \"model\": \"OperationRepo.review\", \"fields\": {\"date\": \"2011-10-05\", \"text\": \"Wow, the number of flat screens in this bar would impress the football gods! I felt really welcomed when I visited Blue 32 -- it wasn't too rowdy nor too quiet either. \\n\\nI ordered the Black and Blue burger, which definitely hit the spot. Though, I do need to get my butt back to the gym. Regardless, bleu cheese and bacon on a burger -- how can you say No!? It was cooked perfectly and with fat yummy fries on the side. Didn't order a drink unfortunately this time since my weekend hangover was still lingering haha! \\n\\nService was okay; we were greeted with a smile. Though I'm always irked when I have to wait for my water to be filled, but all is well.\\n\\nThe ambience was real chill for a sports bar, but like I said not too rowdy is good for me. I like the spot lighting and the booth and bar separation was perfect. - Enjoy!\", \"stars\": 4.0, \"user\": \"XqMkm-DD9VsdcKx2YVGhSA\", \"business\": \"01cEFI5Pq_RyEwM3GSTopQ\"}}]", "[]", "[]"]}
        self.assertTrue(content == actual)

print ("Done")