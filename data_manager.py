import requests
from pprint import pprint
class DataManager:
    def __init__(self):
        self.getresponse = requests.get(url="https://api.sheety.co/5843be2185b02f97b1f6fc8d2a584dfa/flightDeals/prices")
        self.length = len(self.getresponse.json()['prices'])
        self.prices = self.getresponse.json()['prices']
        self.putresponse = ""
        self.body = {}

    def put(self, sheet_data):
        for i in range(len(sheet_data)):
            self.body = {
                'price': {
                    "iataCode": f"{sheet_data[i]['iataCode']}"
                }
            }
            self.putresponse = requests.put(
                url=f"https://api.sheety.co/5843be2185b02f97b1f6fc8d2a584dfa/flightDeals/prices/{sheet_data[i]['id']}",
                json=self.body)



