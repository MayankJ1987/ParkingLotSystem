from app.entities.vehicle import Vehicle, Car, Bus, Bike
from app.entities.vehicle_type import VehicleType
from app.entities.slot import Slot
from app.entities.level import Level
from app.entities.parking_lot import ParkingLot

if __name__ == "__main__":
    try:
        print("Parking Lot System")

        car = Car('AOBO 2247', 'XYZ Solutions Pvt. Ltd.')
        # print('Car details ############')
        # print('Plate Number : ' + str(car.get_plat_number()))
        # print('Company Name : ' + str(car.get_company_name()))
        # print('Vehicle Type : ' + str(car.get_vehicle_type()))

        bus = Bus('BOCO 2280', 'XYZ Solutions Pvt. Ltd.')
        # print('Bus details ############')
        # print('Plate Number : ' + str(bus.get_plat_number()))
        # print('Company Name : ' + str(bus.get_company_name()))
        # print('Vehicle Type : ' + str(bus.get_vehicle_type()))

        bus1 = Bus('CODO 2240', 'PSQ Solutions Pvt. Ltd.')

        # Slot1
        slot1 = Slot(1, 2, VehicleType.CAR)
        # # print('Slot1 details ############')
        # # print('Slot for Vehicle Type : ' + str(slot1.get_type_of_vehicle()))
        # # print('Vehicle Parked : ' + str(slot1.get_vehicle()))
        # # print('Slot Available : ' + str(slot1.is_available()))
        #
        # # # Trying to park Bus
        # # print('Trying to park Bus ############')
        # # slot1.park_vehicle(bus)
        # # #print(slot1.get_vehicle())  # get_plate_number())
        # # print('Slot Available : ' + str(slot1.is_available()))
        # #
        # # print('Trying to park Car ############')
        # # slot1.park_vehicle(car)
        # # print(slot1.get_vehicle()) #get_plate_number())
        # # print('Slot Available : ' + str(slot1.is_available()))
        # #
        # # print('Exit vehicle ############')
        # # slot1.exit_vehicle()
        # # print('Slot Available : ' + str(slot1.is_available()))

        slot2 = Slot(1, 2, VehicleType.CAR)

        level1 = Level(1, 2, 2)
        level1.add_slot(slot1)
        level1.add_slot(slot2)
        #
        # print('Parking car ############')
        # level1.park_vehicle(car)
        # # level1.park_vehicle(bus)
        # print('Parked vehicles for XYZ company : ' + str(level1.company_parked_vehicles('XYZ Solutions Pvt. Ltd.')))
        #
        # print('Parking bus1 ############')
        # level1.park_vehicle(bus1)
        # print('Parked vehicles for XYZ company : ' + str(level1.company_parked_vehicles('XYZ Solutions Pvt. Ltd.')))
        # print('Parked vehicles for PSQ company : ' + str(level1.company_parked_vehicles('PSQ Solutions Pvt. Ltd.')))

        slot3 = Slot(1, 2, VehicleType.BUS)
        slot4 = Slot(1, 2, VehicleType.CAR)
        level2 = Level(1, 2, 2)
        level2.add_slot(slot3)
        level2.add_slot(slot4)

        slot5 = Slot(1, 2, VehicleType.CAR)
        slot6 = Slot(1, 2, VehicleType.BUS)
        level3 = Level(1, 2, 2)
        level3.add_slot(slot5)
        level3.add_slot(slot6)

        parking_lot = ParkingLot(3)
        parking_lot.add_level(level1)
        parking_lot.add_level(level2)
        parking_lot.add_level(level3)

        print('############ Parking car ############')
        parking_lot.park_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(len(parking_lot.company_parked_vehicles('XYZ Solutions '
                                                                                                   'Pvt. Ltd.'))))

        print('\n############ Exiting car ############')
        parking_lot.exit_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(len(parking_lot.company_parked_vehicles('XYZ Solutions '
                                                                                                   'Pvt. Ltd.'))))

        print('############ Parking Bus ############')
        # parking_lot.park_vehicle(bus)

        print('############ ############ 2nd scenario ############ ############')
        parking_lot = ParkingLot(3)
        parking_lot.add_level(level1)
        parking_lot.add_level(level1)
        parking_lot.add_level(level1)

        print('############ Parking car ############')
        parking_lot.park_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(
            len(parking_lot.company_parked_vehicles('XYZ Solutions Pvt. Ltd.'))))

        print('\n############ Exiting car ############')
        parking_lot.exit_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(
            len(parking_lot.company_parked_vehicles('XYZ Solutions Pvt. Ltd.'))))

        print('############ ############ 3rd scenario ############ ############')
        car = Bus('AOBO 2247', 'XYZ Solutions Pvt. Ltd.')
        parking_lot = ParkingLot(3)
        parking_lot.add_level(level1)
        parking_lot.add_level(level1)
        parking_lot.add_level(level1)

        print('############ Parking car ############')
        parking_lot.park_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(
            len(parking_lot.company_parked_vehicles('XYZ Solutions Pvt. Ltd.'))))

        print('\n############ Exiting car ############')
        parking_lot.exit_vehicle(car)
        print('\nParked vehicles for XYZ company : ' + str(
            len(parking_lot.company_parked_vehicles('XYZ Solutions Pvt. Ltd.'))))

    except Exception is e:
        print(f'Exception is {str(e)}')

else:
    print("Go to Hell")
