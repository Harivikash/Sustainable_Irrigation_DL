
# **** SOME MORE WORK IS LEFT ****
# Not accurate
# need GPS module 

from geopy.geocoders import Nominatim
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def get_ip_address():
    try:
        # Get the hostname of the device
        hostname = socket.gethostname()

        # Get the IP address associated with the hostname
        ip_address = socket.gethostbyname(hostname)

        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
        return ip_address
    except Exception as e:
        print(f"Error: {e}")

def get_location():
    # geolocator = Nominatim(user_agent="geo_locator")
    your_location=get_ip_address()
    res=DbIpCity.get(your_location, api_key="free")
    location = res.city
    
    print("Location details:")
    print(f"Latitude: {res.latitude}")
    print(f"Longitude: {res.longitude}")
    print(f"Address: {res.city}")
    return [res.latitude, res.longitude]

# if __name__ == "__main__":
#     get_location()
