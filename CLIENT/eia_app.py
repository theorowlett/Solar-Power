import requests
from dotenv import load_dotenv
import json
import os
from pprint import pprint
from numpy import polyfit, array

def main():
    statename = get_state()
    data = get_data(statename)
    pprint(data['slope'])
    exit()

def get_state():
    statename = input('Enter the 2 letter state code: ')
    return statename

def get_data(statename):
    load_dotenv()
    EIA_KEY = os.getenv('EIA_KEY')
    url = 'http://api.eia.gov/series/'
    payload = {
        'api_key' :EIA_KEY,
        'series_id' : 'ELEC.PRICE.' + statename + '-ALL.A'
    }

    r = requests.get(url,params=payload)
    j = json.loads(r.text)
    previous_costs = j['series'][0]['data']
    year = []
    price = []
    for i in range(len(previous_costs)):
        year.append(int(previous_costs[i][0]))
        price.append(previous_costs[i][1])
    year = array(year)
    price = array(price)
    m, b = polyfit(year,price,1)
    data = {
        'year' : year,
        'price' : price,
        'slope' : m,
        'intercept' : b,
    }
    return data

if __name__=='__main__':
    main()