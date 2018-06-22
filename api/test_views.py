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

    def test_get_all_clients(self):
        """
        method for testing get all rides
        """
        result = self.client().get('api/v1/rides')

        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["rides"])
   