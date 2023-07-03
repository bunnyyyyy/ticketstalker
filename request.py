import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

# PRODUCT_URL_CSV = "products.csv"
# SAVE_TO_CSV = True
# PRICES_CSV = "prices.csv"
# SEND_MAIL = True




def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    return df



def get_response(url):
    response = requests.get(url)
    return response.text


info = get_response("https://seatgeek.com/taylor-swift-with-haim-and-gracie-abrams-tickets/santa-clara-california-levi-s-stadium-2023-07-28-6-30-pm/concert/5862048")


f = open("info.txt", "w")
f.write(info)
f.close()






def get_price(html):
    soup = BeautifulSoup(html, "lxml")
    el = soup.select_one(".price_color")
    price = Price.fromstring(el.text)
    return price.amount_float