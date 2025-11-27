
import data
#NEED TO INPUT ACTUAL DATA
#TEMP DATA AS OF 11/27/2025
energy_data =  [data.Room(201, 10000.5, 20005.7,
                         3000.15, 200.5, 1905.67).to_dict(),
                data.Room(202, 9701.41, 16300.59,
                         2700.41, 676.76, 4121.25).to_dict(),
                data.Room(204, 15090,17358.98, 22255.97,
                         3020.47, 1000.67).to_dict()
                ]






def calculate_average_all():
    avg_dict = {"Shower Energy": 0, "Light Energy": 0, "Fan Energy": 0,
                "Air Purifier Energy": 0, "Device Energy": 0}
    for room in energy_data:
        for room_data in avg:
            if room_data in avg_dict:
                avg_dict[room_data] += room[room_data]

    for key in avg_dict:
        avg_dict[key] = avg_dict[key] / len(energy_data)
    return ("Average Shower Energy: {}, Average Light Energy: {}, Average Fan Energy: {}, Average Air Purifier Energy: {}, Average Device Energy: {}").format()

def find_above_average():

def total_energy_average():