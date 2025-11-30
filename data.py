# dictionaries to hold placeholders for the wattage that each thing uses for calculations

# NEED TO FIGURE OUT HOW TO DO MULTIPLE TYPES OF DEVIECES, OR MULTIPLE TYPES OF FANS ETC

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
                 fan_type: str,
                 fan_hours: float,
                 ap_hours: float,
                 ap_type: str,
                 device_type: str,
                 device_hours: float):

        self.room_num = room_num
        self.shower_watts = shower_watts
        self.shower_hours = shower_hours
        self.light_watts = light_watts
        self.light_hours = light_hours
        self.fan_type = fan_type
        self.fan_hours = fan_hours
        self.ap_hours = ap_hours
        self.ap_type = ap_type
        self.device_type = device_type
        self.device_hours = device_hours

# need to fix these two methods

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
    def shower_energy(self):
        return self.shower_watts * self.shower_hours

    # same thing but for lights (they can b set number as same lights and showers)
    def light_energy(self):
        return self.light_watts * self.light_hours

    # multiply the amt of hours by the wattage of a type of fan inputed (ie fan1 fan2 etc.)
    def fan_energy(self):
        return fan_watts[self.fan_type] * self.fan_hours

    # same thing but for ap
    def ap_energy(self):
        return ap_watts[self.ap_type] * self.ap_hours

    # same thing but for devices
    def device_energy(self):
        return device_watts[self.device_type] * self.device_hours





