from views import Get_ride


class Get_urls:
    @staticmethod
    def fetch_urls(ride):
        

        All_rides_view = Get_ride.as_view('All_rides')
        One_ride_view = Get_ride.as_view('Specific_ride')

        ride.add_url_rule('/api/v1/rides', view_func=All_rides_view, defaults={'name': None}, methods=['GET',])
        ride.add_url_rule('/api/v1/rides/<string:name>', view_func=One_ride_view, methods=['GET',])
        ride.add_url_rule('/api/v1/rides', view_func=One_ride_view, methods=['POST',])

