import pandas as pd
import requests


class Show:
    def __init__(self, stub_hub_url):
        self.stub_hub_url = stub_hub_url


    

    def get_stubhub_price(self):
        info = requests.get(self.stub_hub_url).text

        f = open("info.txt", "w")
        f.write(info)
        f.close()

        result_string = info[info.find("minPrice") + len("minPrice:"):]
        price = result_string[1:7]
        return price



sc28 = Show("https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/")
print(sc28.get_stubhub_price())