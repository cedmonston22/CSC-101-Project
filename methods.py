
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
        devices=[("laptop", 10), ("phone", 10),
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
                 ("laptop", 10), ("laptop", 10)]
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
                 ("laptop", 12), ("laptop", 12)]
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

def energy_type_average(energy_data: list[dict], energy_type: str):
    avg = 0
    for room in energy_data:
        avg += room[energy_type]
    avg = round(avg / len(energy_data), 2)
    return f"Average {energy_type} usage: {avg} Watts"


def total_energy_average(energy_data: list[dict]):
    total_energy = 0
    for room in energy_data:
        total_energy += room["Shower Energy"]
        total_energy += room["Light Energy"]
        total_energy += room["Fan Energy"]
        total_energy += room["Air Purifier Energy"]
        total_energy += room["Device Energy"]
    return round(total_energy / len(energy_data), 2)

def highest_total_energy(energy_data: list[dict]):
    highest_energy_room = None
    highest_total = -1
    for entry in energy_data:
        total = (
            entry["Shower Energy"] +
            entry["Light Energy"] +
            entry["Fan Energy"] +
            entry["Air Purifier Energy"] +
            entry["Device Energy"]
        )
        if total > highest_total:
            highest_total = total
            highest_energy_room = entry["Room Number"]
    return f"Room {highest_energy_room} has the highest total energy with {highest_total} Watts"

def lowest_total_energy(energy_data: list[dict]):
    lowest_energy_room = None
    lowest_total = float("inf")
    for entry in energy_data:
        total = (
            entry["Shower Energy"] +
            entry["Light Energy"] +
            entry["Fan Energy"] +
            entry["Air Purifier Energy"] +
            entry["Device Energy"]
        )
        if total < lowest_total:
            lowest_total = total
            lowest_energy_room = entry["Room Number"]
    return f"Room {lowest_energy_room} has the lowest total energy with {lowest_total} Watts"
def tips_for_above_average(energy_data: list[dict]):
    pass
# no tips yet right, i'll do this with u later

# added extra, average total energy to main

if __name__ == "__main__":
    print("DAILY ENERGY USAGES:")
    print(energy_type_average(rooms, "Shower Energy"))
    print(find_above_average(rooms, "Shower Energy"))
    print("Tip: Consider taking shorter showers")
    print("")
    print(energy_type_average(rooms, "Light Energy"))
    print(find_above_average(rooms, "Light Energy"))
    print("Tip: Turning off lights when you sleep, or not in the room can conserve energy")
    print("")
    print(energy_type_average(rooms, "Fan Energy"))
    print(find_above_average(rooms, "Fan Energy"))
    print("Tip: Try opening windows if it gets too hot before turning on your fans")
    print("")
    print(energy_type_average(rooms, "Air Purifier Energy"))
    print(find_above_average(rooms, "Air Purifier Energy"))
    print("Tip: Try to utilize a more energy-efficient air purifier or reduce hours when you aren't in the room ")
    print("")
    print(energy_type_average(rooms, "Device Energy"))
    print(find_above_average(rooms, "Device Energy"))
    print("Tip: Try to limit your use of the devices throughout the day so you charge them less, and consider using")
    print("the 80% feature to stop your phones charging at 80% throughout the night")
    print("")
    print("")
    print(lowest_total_energy(rooms))
    print(highest_total_energy(rooms))
    print("")
    print("Average Total Energy:", total_energy_average(rooms), "Watts ")