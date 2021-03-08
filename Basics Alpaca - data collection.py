
import requests, json
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
HEADER = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDER_URL = "{}/v2/orders".format(BASE_URL)
ASSETS_URL = "{}/v2/assets".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADER, )

    return json.loads(r.content)

# holdings = get_account()
# print(holdings)

def create_order(symbol, qty, side, type, time_in_force):
    data ={
        'symbol' : symbol, 
        'qty' : qty, 
        'side' : side, 
        'type' : type, 
        'time_in_force' : time_in_force
    }
    r = requests.post(ORDER_URL, json=data, headers=HEADER, )

    return json.loads(r.content)

# response = create_order("AAPL", 100, "buy", "market", "gtc")

# print(response)


def get_orders():
    r = requests.get(ORDER_URL, headers=HEADER)

    return json.loads(r.content)

# orders = get_orders()

# print(orders)

def get_assets():
    r = requests.get(ASSETS_URL, headers=HEADER)

    return json.loads(r.content)

assets = get_assets()

# Searching the assets variable for Microstrategy :-)
counter = 0
for i in assets:
    
    if "microstrategy" in  i['name'].lower():
        counter += 1
        print("{} - {} - {} - {}".format(counter, i['exchange'], i['symbol'], i['name']))


