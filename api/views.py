from flask import jsonify, request
from flask.views import MethodView

class Get_ride(MethodView):
    rides =[{'name' : 'kalyango','start':'muk','destination':'ntida'},{'name' : 'kalyango2','start':'muk','destination':'ntida'}, {'name' : 'kalyango3','start':'muk','destination':'ntida'}, {'name' : 'kalyango4','start':'muk','destination':'ntida'}]
    def get(self, name):
        if name == None:
            return jsonify({'rides':self.rides})
        rids = [ride for ride in self.rides if ride['name'] == name]
        return jsonify({'ride' : rids[0]})

	    
        