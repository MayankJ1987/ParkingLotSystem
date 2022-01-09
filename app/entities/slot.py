class Slot:
    def __init__(self, lane_number, slot_number, type_of_vehicle):
        self.lane_number = lane_number
        self.slot_number = slot_number
        self.type_of_vehicle = type_of_vehicle
        self.vehicle = None
        #self. =

    def get_type_of_vehicle(self):
        return self.type_of_vehicle

    def get_vehicle(self):
        return self.vehicle

    def is_available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle):
        if self.is_available():
            if self.type_of_vehicle == vehicle.get_vehicle_type():
                self.vehicle = vehicle
                # print('Vehicle is parked in a given slot')
                return True
            else:
                # print('Given vehicle is not of a type to vehicle to be parked in the slot')
                return False
        else:
            # print('Slot is full')
            return False

    def exit_vehicle(self):
        self.vehicle = None
        return True
