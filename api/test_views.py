# -*- coding: utf-8 -*-
"""This is the main module"""
import unittest
import json
from json import JSONEncoder

from app import APP
class TestViews(unittest.TestCase):
    """
    Class defines test cases
    """
    def setUp(self):
        """
        initializing
        """
        self.ride = APP
        self.client = self.ride.test_client
    def test_get_all_clients(self):
        """
        method for testing get all rides
        """
        result = self.client().get('api/v1/rides')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["rides"])

    def test_get_specific_ride(self):
        """
        tesing for get specific ride
        """
        result = self.client().get('api/v1/rides/2')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["ride"])
    def test_create_ride(self):
        """
        tesing for create ride
        """
        result = self.client().post('api/v1/rides', content_type="application/json", data=json.dumps(dict(id=4, time_to_leave="1:29 pm", price="4000 /=", start="Gayaza", destination="matuga", Driver_name="kalyango john")))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["rides"])
        self.assertIn('time_to_leave', str(result.data))
    def test_requests(self):
        """
        testing for request to join a ride
        """
        result = self.client().post('/api/v1/rides/2/requests', content_type="application/json", data=json.dumps(dict(id=4, passenger_name="Junior Sara", phone_number="078966857")))
        
        self.assertTrue(result.json["reqs"])
        self.assertIn(b"ride_id", result.data)
        
