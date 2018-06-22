# -*- coding: utf-8 -*-
"""This is the main module"""
import unittest
import json
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
    def test_requests(self):
        """
        testing for request to join a ride
        """
        result = self.client().post('/api/v1/rides/2/requests', content_type="application/json", data=json.dumps(dict(id=4, passenger_name="Junior Sara", phone_number="078966857")))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["requests"])
        self.assertIn(b"ride_id", result.data)
