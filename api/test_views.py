import unittest 
 
from app import APP

class TestViews(unittest.TestCase):
    ri =[
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        ]
    def setUp(self):
        self.ride = APP 
        self.client = self.ride.test_client
        self.bucketlist = {'name': 'Go to Borabora for vacation'}
    def test_get_all_clients(self):
        result = self.client().get('api/v1/rides')
       
        self.assertEqual(result.status_code, 200)
        # self.assertEqual(result.get(name == None), ri)
      

    