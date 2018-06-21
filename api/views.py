# -*- coding: utf-8 -*-
"""Module defines views """
from flask import jsonify, request
from flask.views import MethodView
class GetRide(MethodView):
    """
    class that defines views
    """
    reqs = [
        {'id':1, 'ride_id':4, 'passenger_name':'Peter', 'phone_number':'0752067415'},
        {'id':2, 'ride_id':1, 'passenger_name':'Peter', 'phone_number':'0782699260'},
        {'id':3, 'ride_id':3, 'passenger_name':'Peter', 'phone_number':'0757597843'},
        ]
  
    def post(self, ride_id):
        """
        method for all post requests
        """
        if not request.json:
            return jsonify({'error' : "not a json request"}), 400
        req = {'id':request.json['id'], 'ride_id':ride_id, 'passenger_name':request.json['passenger_name'], 'phone_number':request.json['phone_number']}
        self.reqs.append(req)
        return jsonify({'requests' : self.reqs})
        