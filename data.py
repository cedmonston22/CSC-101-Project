# dictionaries to hold placeholders for the wattage that each thing uses for calculations

# NEED TO FIGURE OUT HOW TO DO MULTIPLE TYPES OF DEVIECES, OR MULTIPLE TYPES OF FANS ETC
# commit

fan_watts = {"woozoo": 1.0, "hurricane": 2.0, "idk": .5, "example": 0.0} #all placeholders
ap_watts = {"winix": 5.0, "blue pure": 3.0, "idk": .5, "example": 0.0} #all placeholders
device_watts = {"phone": 1.0, "mac": 3.0, "laptop": 5.0, "ipad": 2.0} #all placeholders



class Room:
    def __init__(self,
                 room_num: int,
                 shower_watts: float,
                 shower_hours: float,
                 light_watts: float,
                 light_hours: float,
                 fans: list[tuple(str, int)],
                 air_purifiers: list[tuple(str, int)],
                 devices: list[dict],
                 ):

        self.room_num = room_num
        self.shower_watts = shower_watts
        self.shower_hours = shower_hours
        self.light_watts = light_watts
        self.light_hours = light_hours

        self.fans = [(fan_type.lower(), hrs) for fan_type, hrs in fans]
        self.air_purifiers = [(air_purifier_type.lower(), hrs) for air_purifier_type, hrs in air_purifiers]
        self.devices = [(device_type.lower(), hrs) for device_type, hrs in devices]


    def __repr__(self):
        return (("Room Number: {}, Shower Energy: {}, Light Energy: {}, Fan Energy: {}, "
                "Air Purifier Energy: {}, Device Energy: {}")
                .format(self.room_num, self.shower_energy(), self.light_energy(), self.fan_energy(),self.ap_energy(),self.device_energy()))

    def to_dict(self):
        return{"Room Number": self.room_num, "Shower Energy": self.shower_energy(), "Light Energy": self.light_energy(),
               "Fan Energy": self.fan_energy(), "Air Purifier Energy": self.ap_energy(), "Device Energy": self.device_energy()}

# energy calculations
    # multiplying the shower wattage you input, or we can just have it set,
    # by the amount of hours to get wattage per hour (can use different unit)

    # make sure if somethign different is enetered, the whole thing dosen't crash
    def lookup(self, table: dict, key: str):
        return table.get(key, 0)

    def shower_energy(self):
        return self.shower_watts * self.shower_hours

    # same thing but for lights (they can b set number as same lights and showers)
    def light_energy(self):
        return self.light_watts * self.light_hours

    # multiply the amt of hours by the wattage of a type of fan inputed (ie fan1 fan2 etc.)
    def fan_energy(self):
        total = 0
        for fan_type, hrs in self.fans:
            total += self.lookup(fan_watts, fan_type) * hrs
        return total

    # same thing but for ap
    def ap_energy(self):
        total = 0
        for air_purifier_type, hrs in self.air_purifiers:
            total += self.lookup(ap_watts, air_purifier_type) * hrs
        return total

    # same thing but for devices
    def device_energy(self):
        total = 0
        for device_type, hrs in self.devices:
            total += self.lookup(device_watts, device_type) * hrs
        return total





