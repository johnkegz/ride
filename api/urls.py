# -*- coding: utf-8 -*-
"""
Module decorates views to urls
"""
from views import GetRide
class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(ride):
        """
        Method that views with urls
        """
        rides_view_update = GetRide.as_view('rides_update')
        ride.add_url_rule('/api/v1/rides', defaults={'ride_id': None}, view_func=rides_view_update, methods=['POST',])
     