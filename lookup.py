# importing modules

import requests
import json
import os

os.system('clear')

# connecting the coinmarketcap api to pull the data

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")

# parsing into json and storing in new variable

api = json.loads(api_request.content)

# sample test to check if the data is present -> print(api)

# creating a list of cryptocurrencies

currencies = ["BTC", "XRP", "ETH", "MIOTA", "LTC"]

# looping through the ticker to get data of the currencies that we need

print("-- Report on Cryptocurrencies --")
for keys in api:
    for coin in currencies:
        if coin == keys["symbol"]:
            print("Name: \t\t" + keys["name"])
            print("Price in USD: \t" + "${0:.2f}".format(float(keys["price_usd"])))
            print("Rank: \t\t" + keys["rank"])
            print("-----------------------")
