# -*- coding: utf-8 -*-
"""Module defines views """
from flask import jsonify, request
from flask.views import MethodView
class GetRide(MethodView):
    """
    class that defines views
    """
    rides = [
        {'id':1, 'time_to_leave' : '12:30 pm', 'price':'5000/=', 'start':'makerere', 'destination':'Bukoto', 'Driver_name':'Mutano Jude'},
        {'id':2, 'time_to_leave' : '12:30 pm', 'price':'400/=', 'start':'Kikoni', 'destination':'Munyonyo', 'Driver_name':'Mutano jude'},
        {'id':3, 'time_to_leave' : '12:30 pm', 'price':'25000/=', 'start':'Ntinda', 'destination':'Makerere', 'Driver_name':'Faith Shella'},
        {'id':4, 'time_to_leave' : '12:30 pm', 'price':'500/=', 'start':'makerere', 'destination':'Ntida', 'Driver_name':'Faith Shella'},
        ]
    def post(self, ride_id):
        """
        method for all post requests
        """
        if not request.json:
            return jsonify({'error' : "not a json request"}), 400
        if ride_id == None:
            ride = {'id':request.json['id'], 'time_to_leave' : request.json['time_to_leave'], 'price':request.json['price'], 'start':request.json['start'], 'destination':request.json['destination'], 'Driver_name':request.json['Driver_name']}
            self.rides.append(ride)
            return jsonify({'rides' : self.rides})
                       