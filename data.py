class EnergyPerRoom:
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
        return (("Room {} Energy Usage - Shower: {}, Lights: {}, Fans: {}, "
                "Air Purifiers: {}, Devices: {}")
                .format(self.room_num, self.shower_energy, self.light_energy, self.fan_energy,self.ap_energy,self.device_energy))


