# --------------- Importing Modules ---------------

from tkinter import *
import requests
import json
import os

os.system('clear')

root = Tk()

root.title("Cryptofolio")
root.tk_setPalette(background = "gray14" , foreground = "SteelBlue1")

# --------------- Start Header ---------------
i = 0


header = ["Name", "Rank", "Current Price", "Price Paid", "Current Value", "Profit/Loss per hour", "Profit/Loss total", "1 Hour Change", "24 Hour Change", "7 Day Change" ]

for x in header:
    name = Label(root, text ="|" + x + "|", font = "Zwizz")
    name.grid(row = 0, column = i, sticky = N+S+E+W, ipadx = 5)
    i+=1

# --------------- End Header ---------------


total_profit_loss_value = 0

def lookup():

    # connecting the coinmarketcap api to pull the data

    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")

    # parsing into json and storing in new variable

    api = json.loads(api_request.content)

    # creating a list of cryptocurrencies

    currencies = ["BTC", "XRP", "ETH", "MIOTA", "LTC"]

    # --------------- Creating the Portfolio ---------------

    my_portfolio = [
        {
            "sym": "BTC",
            "amount_owned" : 20,
            "price_paid_per_coin": 500,

        },
        {
            "sym": "ETH",
            "amount_owned" : 5,
            "price_paid_per_coin": 90,

        },
        {
            "sym": "XRP",
            "amount_owned" : 50,
            "price_paid_per_coin": 1.80,

        },
        {
            "sym": "LTC",
            "amount_owned" : 4,
            "price_paid_per_coin": 30,

        },
        {
            "sym": "MIOTA",
            "amount_owned" : 120,
            "price_paid_per_coin": 0.90,

        }
    ]

    total_profit_loss_value = 0
    j = 0
    i = 0
    # looping through the ticker to get data of the currencies that we need
    print("-- Report on Cryptocurrencies --")
    for keys in api:
        for coin in my_portfolio:

            # Finding Total amount paid
            total_amount_paid = float(coin["amount_owned"]) * float(coin["price_paid_per_coin"])
            current_value = float(coin["amount_owned"])* float(keys["price_usd"])
            profit_loss_value = current_value - total_amount_paid
            total_profit_loss_value+=profit_loss_value
            profit_loss_per_coin = float(keys["price_usd"]) - float(coin["price_paid_per_coin"])

            #if coin["sym"] == keys["symbol"]:
            #    print("Name: \t\t" + keys["name"])
            #    print("Price in USD: \t" + "${0:.2f}".format(float(keys["price_usd"])))
            #    print("Total Amount Paid: \t" + "${0:.2f}".format(float(total_amount_paid)))
            #    print("Profit / Loss: \t" + "${0:.2f}".format(float(profit_loss_value)))
            #    print("Profit / Loss per coin: \t" + "${0:.2f}".format(float(profit_loss_per_coin)))
            #    print("-----------------------")

            data = [keys["name"], keys["rank"], keys["price_usd"], total_amount_paid, current_value, profit_loss_value, total_profit_loss_value, keys["percent_change_1h"], keys["percent_change_24h"], keys["percent_change_7d"] ]

            name_coin = Label(root, text=keys["name"], font = "Zwizz")
            name_coin.grid(row = row_count, column = 0, sticky = N+S+E+W, ipadx = 5)

            rankcoin = Label(root, text=keys["rank"], font = "Zwizz")
            rankcoin.grid(row = row_count, column = 1, sticky = N+S+E+W, ipadx = 5)

            pricecoin = Label(root, text="${0:.2f}".format(float(keys["price_usd"], font = "Zwizz")
            pricecoin.grid(row = row_count, column = 2, sticky = N+S+E+W, ipadx = 5)







    #print("Total Profit / Loss: \t" + "${0:.2f}".format(float(total_profit_loss_value)))


# instantiating the function / refreshing the window
lookup()
root.mainloop()
