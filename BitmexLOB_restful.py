import requests, json
import pandas as pd
import os

BASE_URL = "https://www.bitmex.com/api/v1"
ORDER_BOOK = "{}/orderBook/L2".format(BASE_URL)

params = {
    "symbol" : "XBTUSD",
    "depth" : 25
}

# Function that collects a single 25 level excerpt of Bitcoin Perp contract limit order book
def orderBookSnapShot():
    response = requests.get(ORDER_BOOK,params=params)
    r = json.loads(response.content)
    columns = ['symbol', 'id', 'side', 'size', 'price']
    data_list = []
    for i in r:
        data_list.append(i)
    df = pd.DataFrame(data_list)
    return df.to_csv(os.getcwd() + "\\excerpt.csv")

orderBookSnapShot()

