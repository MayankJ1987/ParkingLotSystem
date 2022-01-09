class Level:
    def __init__(self, floor_number, slots_per_lane, no_of_lanes):
        self.floor_number = floor_number
        self.no_of_slots = slots_per_lane * no_of_lanes
        self.slots = list()

    def add_slot(self, slot):
        if len(self.slots) + 1 <= self.no_of_slots:
            print('Slot added in a level')
            self.slots.append(slot)
        else:
            print('Level is full. No slot can be added further')

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if slot.park_vehicle(vehicle):
                # print('Vehicle is parked in a slot in a level')
                # self.available_slots.remove(slot)
                # self.parked_slots.add(slot)
                return True
        # print('Level is Full or Unable to park vehicle in a slot in a level')
        return False

    def exit_vehicle(self, vehicle):
        for slot in self.slots:
            if slot.get_vehicle() is not None and \
                    slot.get_vehicle().get_plate_number() == vehicle.get_plate_number():
                slot.exit_vehicle()
                # self.parked_slots.remove(slot)
                # self.available_slots.add(slot)
                # print('Vehicle is removed from the slot in a given level')
                return True
        # print('Vehicle is not parked in the slot in a given level')
        return False

    def company_parked_vehicles(self, company_name):
        vehicle_list = list()
        for slot in self.slots:
            if slot.get_vehicle() is not None and \
                    slot.get_vehicle().get_company_name() == company_name:
                vehicle_list.append(slot.get_vehicle())
        #return len(vehicle_list)
        return vehicle_list
