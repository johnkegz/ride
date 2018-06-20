import unittest 

from app import APP

class TestViews(unittest.TestCase):
    ri = {'name' : 'kalyango','start':'muk','destination':'ntida'},
         
         
    def setUp(self):
        self.ride = APP 
        self.client = self.ride.test_client
        
    def test_get_all_clients(self):
        result = self.client().get('api/v1/rides')
       
        self.assertEqual(result.status_code, 200)
        #self.assertEqual(result.status_code, 404)
        #self.assertIn("kalyang", result.data)
    def test_get_specific_ride(self):    
        result = self.client().get('api/v1/rides/9')
        self.assertEqual(result.status_code, 200)
    
      

    