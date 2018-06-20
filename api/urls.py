from views import Get_ride


class Get_urls:
    @staticmethod
    def fetch_urls(APP):
        

        rides_view = Get_ride.as_view('ride_my_way')

        rides.add_url_rule('/api/v1/rides', view_func=rides_view, defaults={'id': None}, method=['Get',])

