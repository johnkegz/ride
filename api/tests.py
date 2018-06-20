import unittest 
 
from app import APP

class TestViews(unittest.TestCase):
    def setUp(self):
        self.ride = APP 
        self.client = self.ride.test_client
    def get_all_clients(self):
        result = self.client().get('api/v1/ride')
       
        self.assertEqual(result.status_code, 200)
if __name__ == '__main__':
    unittest.main()
    