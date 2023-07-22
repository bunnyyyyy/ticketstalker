import json
import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price



def get_response(url):
    response = requests.get(url)
    return response.text


def get_stubhub_price():

    info = get_response("https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/")
    result_string = info[info.find("minPrice") + len("minPrice:"):]
    price = result_string[1:7]
    return price


