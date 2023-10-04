import requests

SHEETY_ENDPOINT_40 = "https://api.sheety.co/5ca3135dd8eec0f8c2feea42d263d450/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_destinations(self):
        """        Typical Response:
                {'prices':
                    [{'city': 'Moscow', 'iataCode': 'MOW',  'lowestPrice': 54, 'id': 2},
                    {'city': 'Dubai', 'iataCode': 'DXB', 'lowestPrice': 42, 'id': 3},
                    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}]}
                    Typical Output:
                [['Moscow', 'MOW', 54], ['Dubai', 'DXB', 42], ['Tokyo', 'TYO', 485]]
"""
        sheet_response = requests.get(SHEETY_ENDPOINT_40)
        destinations = [[k["city"], k["iataCode"], k['lowestPrice']] for k in sheet_response.json()["prices"]]
        return destinations

    pass
