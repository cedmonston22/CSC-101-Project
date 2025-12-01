
import data

# NEW TEMP DATA (11/29)
temp_data =  [data.Room(201, 100, 1,
                         100, 10, "woozoo", 6, 24, "winix", "laptop", 3), data.Room(202, 100, 5,
                         100, 18, "hurricane", 5, 0, "idk", "phone", 8), data.Room(205, 100, 3,
                         100, 24, "idk", 2, 3, "blue pure", "mac", 12),
                ]

temp_rooms = [room.to_dict() for room in temp_data]



# 3 methods

def calculate_average_all(energy_data: list[dict]):
    avg_dict = {"Shower Energy": 0, "Light Energy": 0, "Fan Energy": 0,
                "Air Purifier Energy": 0, "Device Energy": 0}
    for room in energy_data:
        for key in avg_dict:
            avg_dict[key] += room[key]

    for key in avg_dict:
        avg_dict[key] = round(avg_dict[key] / len(energy_data), 2)
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
        total_energy += room["Shower Energy"]
        total_energy += room["Light Energy"]
        total_energy += room["Fan Energy"]
        total_energy += room["Air Purifier Energy"]
        total_energy += room["Device Energy"]
    return round(total_energy / len(energy_data), 2)

def tips_for_above_average(energy_data: list[dict]):
    pass
# no tips yet right, i'll do this with u later

# added extra, average total energy to main

if __name__ == "__main__":
    print(find_above_average(temp_rooms, "Shower Energy"))
    print(find_above_average(temp_rooms, "Device Energy"))
    print("Average Total Energy:", total_energy_average(temp_rooms))