import unittest 
 
from app import APP

class TestViews(unittest.TestCase):

    def setUp(self):
        self.ride = APP 
        self.client = self.ride.test_client
    def test_get_all_clients(self):
        result = self.client().get('api/v1/rides')
       
        self.assertEqual(result.status_code, 200)
      

    