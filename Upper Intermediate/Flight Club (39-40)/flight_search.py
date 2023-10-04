import requests

FLIGHT_KEY = "eGb_gKQMEOEakMuEci9bwBTwiscI6jnH"
FLIGHT_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'


# [['Moscow', 'MOW', 54], ['Dubai', 'DXB', 42], ['Tokyo', 'TYO', 485]]
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def all_flights(self, data, date_from, date_to, fly_from="LHR", nights_in_dst_from=6, nights_in_dst_to=13):
        return [get_flight(dest[1], date_from, date_to, fly_from, nights_in_dst_from, nights_in_dst_to) for dest in
                data]

    pass


def get_flight(destination, date_from, date_to, fly_from="LHR", nights_in_dst_from=6, nights_in_dst_to=13):
    # destination_list = [el[1] for el in destination]
    params = {
        'fly_from': fly_from,
        # 'fly_from' "LON", # as alternative
        'fly_to': destination,
        "date_from": date_from,  # dd/mm/yy
        "date_to": date_to,  # dd/mm/yy
        'nights_in_dst_from': nights_in_dst_from,
        'nights_in_dst_to': nights_in_dst_to,
        'ret_from_diff_city': False,
        'ret_to_diff_city': False,
        "selected_cabins": "W",
        "curr": "GBP",

    }
    header = {
        "apikey": FLIGHT_KEY,
    }
    response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=header)
    best_flights_dict = {}
    if response.json()['data']:
        date = response.json()['data'][0]['local_departure'][:10]
        best_flights_dict[date] = response.json()['data'][0]
        overall_best_price = best_flights_dict[date]['price']
    else:
        print(f"No data for {destination}")
        return {destination: "No direct flights"}

    for flight in response.json()['data']:
        if flight['local_departure'][:10] in best_flights_dict.keys():
            if flight['price'] < best_flights_dict[flight['local_departure'][:10]]['price']:
                best_flights_dict[flight['local_departure'][:10]] = flight
                overall_best_price = min(flight['price'], overall_best_price)
        else:
            best_flights_dict[flight['local_departure'][:10]] = flight
            overall_best_price = min(flight['price'], overall_best_price)
    return best_flights_dict
