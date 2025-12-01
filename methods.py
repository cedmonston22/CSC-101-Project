
import data
from data import Room
#
# NEW TEMP DATA (11/29) 8
data = [
    data.Room(
        201, 1.25, 12,
        fans=[("hurricane", 24)],
        air_purifiers=[("blue pure", 24), ("blue pure", 24)],
        devices=[("laptop", 8), ("laptop", 8), ("laptop", 8),
                 ("phone", 8), ("phone", 8), ("phone", 8)]
    ),
    data.Room(
        202, 0.75, 9,
        fans=[("woozoo", 6), ("woozoo", 6)],
        air_purifiers=[],
        devices=[("laptop", 10), ("laptop", 10), ("laptop", 10),
                 ("ipad", 10), ("phone", 10), ("phone", 10), ("phone", 10)]
    ),
    data.Room(
        204, 1.5, 18,
        fans=[("idk", 10), ("idk", 10)],
        air_purifiers=[],
        devices=[("mac", 12), ("mac", 12), ("mac", 12),
                 ("phone", 12), ("phone", 12), ("phone", 12)]
    ),
    data.Room(
        205, 1, 12,
        fans=[("woozoo", 24), ("woozoo", 24), ("woozoo", 24)],
        air_purifiers=[("winix", 24)],
        devices=[("laptop", 8), ("laptop", 8), ("laptop", 8),
                 ("ipad", 8), ("ipad", 8), ("phone", 8), ("phone", 8), ("phone", 8)]
    ),
    data.Room(
        206, 2, 16,
        fans=[("woozoo", 24), ("woozoo", 24), ("idk", 24)],
        air_purifiers=[],
        devices=[("laptop", 10), ("laptop", 10), ("laptop", 10),
                 ("phone", 10), ("phone", 10)]
    ),
    data.Room(
        208, 1.5, 16,
        fans=[("woozoo", 6), ("idk", 6)],
        air_purifiers=[("idk", 24)],
        devices=[("laptop", 10), ("phone", 10), ("dj set", 10),
                 ("phone", 10), ("laptop", 10), ("phone", 10),
                 ("laptop", 10), ("phone", 10), ("phone", 10), ("phone", 10)]
    ),
    data.Room(
        209, 1.25, 15,
        fans=[],
        air_purifiers=[],
        devices=[("phone", 10), ("phone", 10), ("phone", 10),
                 ("mac", 10), ("mac", 10), ("mac", 10),
                 ("ipad", 10), ("ipad", 10), ("ipad", 10),
                 ("pc", 10), ("pc", 10)]
    ),
    data.Room(
        210, 0.75, 10,
        fans=[("woozoo", 24), ("woozoo", 24), ("woozoo", 24)],
        air_purifiers=[],
        devices=[("laptop", 15), ("laptop", 15), ("laptop", 15),
                 ("phone", 15), ("phone", 15), ("phone", 15),
                 ("ipad", 15), ("ipad", 15)]
    ),
    data.Room(
        211, 1, 12,
        fans=[("idk", 24), ("idk", 24), ("idk", 24)],
        air_purifiers=[("idk", 24), ("idk", 24)],
        devices=[("mac", 12), ("mac", 12), ("mac", 12),
                 ("phone", 12), ("phone", 12), ("phone", 12)]
    ),
    data.Room(
        212, 1, 18,
        fans=[("woozoo", 24), ("woozoo", 24), ("idk", 24)],
        air_purifiers=[("idk", 24), ("idk", 24)],
        devices=[("mac", 15), ("mac", 15), ("mac", 15),
                 ("ipad", 15), ("ipad", 15), ("ipad", 15),
                 ("phone", 15), ("phone", 15), ("phone", 15), ("phone", 15)]
    ),
    data.Room(
        213, 2, 18,
        fans=[("hurricane", 14), ("idk", 14)],
        air_purifiers=[("idk", 24)],
        devices=[("laptop", 8), ("laptop", 8), ("mac", 8),
                 ("phone", 8), ("phone", 8), ("phone", 8)]
    ),
    data.Room(
        214, 1.5, 24,
        fans=[("woozoo", 24), ("woozoo", 24), ("idk", 24)],
        air_purifiers=[("blue pure", 24), ("blue pure", 24)],
        devices=[("ipad", 12), ("ipad", 12), ("phone", 12),
                 ("phone", 12), ("phone", 12), ("mac", 12),
                 ("mac", 12), ("mac", 12)]
    ),
    data.Room(
        215, 1.25, 16,
        fans=[],
        air_purifiers=[],
        devices=[("phone", 12), ("phone", 12), ("phone", 12),
                 ("ipad", 12), ("ipad", 12), ("ipad", 12),
                 ("mac", 12), ("mac", 12), ("mac", 12),
                 ("pc", 12), ("pc", 12)]
    ),
]

rooms = [room.to_dict() for room in data]



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
    print(find_above_average(rooms, "Shower Energy"))
    print(find_above_average(rooms, "Device Energy"))
    print("Average Total Energy:", total_energy_average(rooms))