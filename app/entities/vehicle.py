from app.entities.vehicle_type import VehicleType

class Vehicle:
    def __init__(self, plat_number, company_name, type_of_vehicle):
        self.__plat_number = plat_number
        self.__company_name = company_name
        self.__type_of_vehicle = type_of_vehicle

    def get_vehicle_type(self):
        return self.__type_of_vehicle

    def get_company_name(self):
        return self.__company_name

    def get_plate_number(self):
        return self.__plat_number

    def set_vehicle_type(self, type_of_vehicle):
        self.__type_of_vehicle = type_of_vehicle

    def set_company_name(self, company_name):
        self.__company_name = company_name

    def set_plat_number(self, VehicleType):
        self.__plat_number = VehicleType

class Car(Vehicle):
    def __init__(self, plat_number, company_name):
        Vehicle.__init__(self, plat_number, company_name, VehicleType.CAR)

class Bus(Vehicle):
    def __init__(self, plat_number, company_name):
        Vehicle.__init__(self, plat_number, company_name, VehicleType.BUS)

class Bike(Vehicle):
    def __init__(self, plat_number, company_name):
        Vehicle.__init__(self, plat_number, company_name, VehicleType.BIKE)
