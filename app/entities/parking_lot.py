class ParkingLot:
    def __init__(self, no_of_levels):
        self.no_of_levels = no_of_levels
        #self.levels = list()
        self.levels = set()

    def add_level(self, level):
        if len(self.levels) + 1 <= self.no_of_levels:
            # self.levels.append(level)
            # self.levels.sort(key=lambda x: x.floor_number)
            self.levels.add(level)
            list(self.levels).sort(key=lambda x: x.floor_number)
            print('Level is successfully added')
        else:
            print('Parking lot is full. No more level is to be added')

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                print('Vehicle is parked in parking lot')
                return True
        print('Vehicle is not parked')
        return False

    def exit_vehicle(self, vehicle):
        for level in self.levels:
            if level.exit_vehicle(vehicle):
                print('Vehicle is exited from parking lot')
                return True
        print('Vehicle is not found')
        return False

    def company_parked_vehicles(self, company_name):
        vehicle_list = list()
        for level in self.levels:
            level_list = level.company_parked_vehicles(company_name)
            if level_list is not None and len(level_list) > 0:
                vehicle_list.append(level_list)
        return vehicle_list
