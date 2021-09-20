import requests
from dotenv import load_dotenv
import json
import os
from pprint import pprint
from numpy import polyfit, array

def main():
    statename = get_state()
    data = get_eia_data(statename)
    pprint(data, indent=2)
    # pprint(data['year'][-1], indent=2)
    exit()

def get_state():
    statename = input('Enter the 2 letter state code: ')
    return statename

def get_eia_data(statename):
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
        'year' : year.tolist(),
        'price' : price.tolist(),
        'best_fit': [],
        # 'slope' : m,
        # 'intercept' : b,
    }
    data['year'].reverse()
    data['price'].reverse()

    for i in range(len(data['year'])+25):
        data['best_fit'].append(m*(data['year'][0]+i)+b)
        if not data['year'][0]+i in data['year']:
            data['year'].append(data['year'][0]+i)
            data['price'].append(0.00)
    
    return data

if __name__=='__main__':
    main()