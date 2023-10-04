class FlightData:

    # This class is responsible for structuring the flight data.

    def __init__(self, flight_dict, destinations):
        self.data = flight_dict
        self.destinations = {k[1]: k[2] for k in destinations}

    def send_data(self):
        with open("destination.txt", mode='w', encoding="UTF-8") as file:
            for el in self.data:
                for k in el.keys():
                    file.writelines(str(el[k]))

                    file.writelines('\n')
            file.writelines('\n')

        with open("destination_cheap.txt", mode='w', encoding="UTF-8") as file:
            for el in self.data:
                # print(self.destinations)
                # print('gothere')
                # print(el)
                for k in el.keys():
                    # print(el[k])
                    if el[k] != 'No direct flights' and (el[k]['price'] < self.destinations[el[k]["cityCodeTo"]]):
                        new_line = f"Flight to {str(el[k]['cityTo'])}," \
                                   f" from {str(el[k]['local_departure'])}" \
                                   f" to {str(el[k]['local_arrival'])}" \
                                   f" priced {str(el[k]['price'])}"
                        file.writelines(new_line)
                        file.writelines('\n')
            pass
