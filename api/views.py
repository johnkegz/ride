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
    reqs = [
        {'id':1, 'ride_id':4, 'passenger_name':'Peter', 'phone_number':'0752067415'},
        {'id':2, 'ride_id':1, 'passenger_name':'Peter', 'phone_number':'0782699260'},
        {'id':3, 'ride_id':3, 'passenger_name':'Peter', 'phone_number':'0757597843'},
        ]
    def get(self, ride_id):
        """
        method for all get requests
        """
        if ride_id == None:
            return jsonify({'rides':self.rides})
        rids = [ride for ride in self.rides if ride['id'] == ride_id]
        return jsonify({'ride' : rids[0]})
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
        req = {'id':request.json['id'], 'ride_id':ride_id, 'passenger_name':request.json['passenger_name'], 'phone_number':request.json['phone_number']}
        self.reqs.append(req)
        return jsonify({'requests' : self.reqs})
