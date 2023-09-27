#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
data_manager = DataManager()


sheet_data = data_manager.prices
# print(sheet_data)
for i in range(len(sheet_data)):
    if sheet_data[i]['iataCode'] == '':
        flight_search = FlightSearch()
        flight_search.iata(sheet_data[i]['city'])
        sheet_data[i]['iataCode'] = flight_search.iata_code
data_manager.put(sheet_data)


now = datetime.now()
tomorrow = now + timedelta(days=1)
to_date = now + timedelta(days=180)
flight_search = FlightSearch()
notification_manager = NotificationManager()

for i in range(len(sheet_data)):
    flight = flight_search.checkflights(sheet_data, tomorrow, to_date)
    if flight.price < sheet_data[i]["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

