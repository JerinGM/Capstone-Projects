import requests
from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.iata_code = ""

    def iata(self, city):
        header = {
            "apikey": "ncraS3FrrAL9K_X7t5gTd_9PbTSOoNxo",
        }
        param = {
            "term": city,
            "location_types": "city"

        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                headers=header,
                                params=param)
        self.iata_code = response.json()["locations"][0]["code"]

    def checkflights(self, sheet_data, tomorrow, to_date):
        header = {
            "apikey": "ncraS3FrrAL9K_X7t5gTd_9PbTSOoNxo",
        }
        param = {
            "fly_from": "LON",
            "fly_to": f"{sheet_data[0]['iataCode']}",
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                                     headers=header, params=param)
        #print(response.json())
        data = response.json()["data"][0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data


