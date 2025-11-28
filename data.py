class Room:
    def __init__(self,
                 room_num: int,
                 shower_energy: float,
                 light_energy: float,
                 fan_energy: float,
                 ap_energy: float,
                 device_energy: float):
        self.room_num = room_num
        self.shower_energy = shower_energy
        self.light_energy = light_energy
        self.fan_energy = fan_energy
        self.ap_energy = ap_energy
        self.device_energy = device_energy

    def __repr__(self):
        return (("Room Number: {}, Shower Energy: {}, Light Energy: {}, Fan Energy: {}, "
                "Air Purifier Energy: {}, Device Energy: {}")
                .format(self.room_num, self.shower_energy, self.light_energy, self.fan_energy,self.ap_energy,self.device_energy))

    def to_dict(self):
        return{"Room Number": self.room_num, "Shower Energy": self.shower_energy, "Light Energy": self.light_energy,
               "Fan Energy": self.fan_energy, "Air Purifier Energy": self.ap_energy, "Device Energy": self.device_energy}

