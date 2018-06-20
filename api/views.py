from flask import jsonify, request
from flask.views import MethodView

class Get_ride(MethodView):
    rides =[
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        {'name' : 'kalyango','start':'muk','destination':'ntida'},
        ]
    def get(self, name):
        if name == None:
            return jsonify({"RideOffer": self.rides})
        