# --------------- Importing Modules ---------------

from tkinter import *
import requests
import json
import os

os.system('clear')

root = Tk()

root.title("Cryptofolio")
root.tk_setPalette(background = "gray14" , foreground = "SteelBlue1")

# --------------- Start GUI Header ---------------
i = 0


header = ["Name", "Rank", "Current Price", "Price Paid", "Current Value", "Profit/Loss per coin", "Profit/Loss total", "1 Hour Change", "24 Hour Change", "7 Day Change" ]

for x in header:
    name = Label(root, text ="|" + x + "|", font = "Zwizz")
    name.grid(row = 0, column = i, sticky = N+S+E+W, ipadx = 5)
    i+=1

# --------------- End GUI Header ---------------


total_profit_loss_value = 0

def red_green(amount):
    if amount >= 0:
        return "SeaGreen2"
    else:
        return "firebrick1"


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
    i = 1
    total_current_value = 0
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
            total_current_value+= current_value

            # --------------- Terminal Output ---------------

            if coin["sym"] == keys["symbol"]:
                print("Name: \t\t" + keys["name"])
                print("Price in USD: \t" + "${0:.2f}".format(float(keys["price_usd"])))
                print("Total Amount Paid: \t" + "${0:.2f}".format(float(total_amount_paid)))
                print("Profit / Loss: \t" + "${0:.2f}".format(float(profit_loss_value)))
                print("Profit / Loss per coin: \t" + "${0:.2f}".format(float(profit_loss_per_coin)))
                print("-----------------------")

            # --------------- GUI Output ---------------

                name = Label(root, text = keys["name"], foreground = "white")
                name.grid(row = i,column=0, sticky = N+S+E+W)

                rank = Label(root, text = keys["rank"], foreground = "VioletRed2")
                rank.grid(row = i,column=1, sticky = N+S+E+W)

                curr_price = Label(root, text = "${0:.2f}".format(float(keys["price_usd"])), foreground = "white")
                curr_price.grid(row = i,column=2, sticky = N+S+E+W)

                price_paid = Label(root, text = "${0:.2f}".format(float(total_amount_paid)), foreground = "white")
                price_paid.grid(row = i,column=3, sticky = N+S+E+W)

                curr_value = Label(root, text = "${0:.2f}".format(float(current_value)), foreground = "SeaGreen2")
                curr_value.grid(row = i,column=4, sticky = N+S+E+W)

                profit_loss_hour = Label(root, text = "${0:.2f}".format(float(profit_loss_per_coin)), foreground = red_green(float(profit_loss_per_coin)))
                profit_loss_hour.grid(row = i,column=5, sticky = N+S+E+W)

                profit_loss_total = Label(root, text = "${0:.2f}".format(float(profit_loss_value)), foreground = red_green(float(profit_loss_value)))
                profit_loss_total.grid(row = i,column=6, sticky = N+S+E+W)

                change_one_hour = Label(root, text = "${0:.2f}".format(float(keys["percent_change_1h"])), foreground = red_green(float(keys["percent_change_1h"])))
                change_one_hour.grid(row = i,column=7, sticky = N+S+E+W)

                change_one_day = Label(root, text = "${0:.2f}".format(float(keys["percent_change_24h"])), foreground = red_green(float(keys["percent_change_24h"])))
                change_one_day.grid(row = i,column=8, sticky = N+S+E+W)

                change_one_week = Label(root, text = "${0:.2f}".format(float(keys["percent_change_7d"])), foreground = red_green(float(keys["percent_change_7d"])))
                change_one_week.grid(row = i,column=9, sticky = N+S+E+W)

                i+=1

            # other features

    porfolio_profit_loss = Label(root, text = "Profit / Loss : ", foreground = "white")
    porfolio_profit_loss.grid(row = i, column = 0, sticky = W, ipadx = 10, ipady = 10)

    porfolio_profit_loss = Label(root, text = "${0:.2f}".format(float(total_profit_loss_value)), foreground = red_green(float(total_profit_loss_value)))
    porfolio_profit_loss.grid(row = i, column = 1, sticky = W, ipadx = 10, ipady = 10)

    root.title("Cryptofolio - Portfolio Value: ${0:.2f}".format(float(total_current_value)))
    print("Total Profit / Loss: \t" + "${0:.2f}".format(float(total_profit_loss_value)))

            # creating the update button

    api = ""
    update_btn = Button(root, text = "Update Prices", command = lookup)
    update_btn.grid(row = i, column = 9, sticky = E+S, ipadx = 10, ipady = 10)

    # --------------- End GUI Output ---------------

# instantiating the function / refreshing the window
lookup()
root.mainloop()
