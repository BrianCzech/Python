from geopy.geocoders import Nominatim
import time
from pprint import pprint

app=Nominatim(user_agent="tutorial")
def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)

address='123 Elm St'
location=get_location_by_address(address)

pprint(location)
latitude=location['lat']
longitude=location['lon']
print(f"{latitude},{longitude}")
