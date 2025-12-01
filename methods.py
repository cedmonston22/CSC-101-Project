
import data
#NEED TO INPUT ACTUAL DATA
#TEMP DATA AS OF 11/27/2025
temp_data =  [data.Room(201, 10000.5, 20005.7,
                         3000.15, 200.5, 1905.67).to_dict(),
                data.Room(202, 9701.41, 16300.59,
                         2700.41, 676.76, 4121.25).to_dict(),
                data.Room(204, 15090,17358.98, 22255.97,
                         3020.47, 1000.67).to_dict()
                ]






def calculate_average_all(energy_data: list[dict]):
    avg_dict = {"Shower Energy": 0, "Light Energy": 0, "Fan Energy": 0,
                "Air Purifier Energy": 0, "Device Energy": 0}
    for room in energy_data:
        for room_data in room:
            if room_data in avg_dict:
                avg_dict[room_data] += room[room_data]

    for key in avg_dict:
        avg_dict[key] = round(avg_dict[key] / len(energy_data),2)
    return avg_dict

def find_above_average(energy_data: list[dict], energy_type: str):
    avg_data = calculate_average_all(energy_data)
    above_average = []
    for room in energy_data:
        if room[energy_type] > avg_data[energy_type]:
            above_average.append(room["Room Number"])
    return f"Rooms with above average {energy_type} usage: {above_average}"


def total_energy_average(energy_data: list[dict]):
    total_energy = 0
    for room in energy_data:
        for room_data in room:
            total_energy += room[room_data]
    return round(total_energy/len(energy_data),2)

def tips_for_above_average(energy_data: list[dict])


if __name__ == "__main__":
    print(find_above_average(temp_data, "Shower Energy"))
    print(find_above_average(temp_data, "Device Energy"))