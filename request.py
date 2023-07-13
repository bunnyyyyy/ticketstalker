import json
import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price






def get_response(url):
    response = requests.get(url)
    return response.text


info = get_response("https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/")


f = open("info.txt", "w")
f.write(info)
f.close()



def get_price(html):
    soup = BeautifulSoup(html, "lxml")
    script_element = soup.find("script", id="index-data")
    if script_element is not None:
        script_content = script_element.string
        json_data = json.loads(script_content)
        min_price_value = json_data["minPrice"]
        return min_price_value
    else:
        return "no index-data id"

print(get_price(info))