import requests
from dotenv import load_dotenv
import json
import os
from pprint import pprint

def main():
    lat = input('Enter the latitude')
    lon = input('Enter the longitude')
    get_nrel_data(lat,lon)

def get_nrel_data(lat=45.5051,lon=-122.6750):
    load_dotenv()
    NREL_KEY = os.getenv('NREL_KEY')
    url = 'https://developer.nrel.gov/api/solar/solar_resource/v1.json'
    payload = {
        'api_key': NREL_KEY,
        'lat': lat,
        'lon': lon,
        'radius' : 0,
    }
    r = requests.get(url,params=payload)
    j = json.loads(r.text)
    # pprint(j['outputs']['avg_ghi']['annual'],indent=2)
    return j['outputs']['avg_ghi']['annual']


if __name__=='__main__':
    main()
