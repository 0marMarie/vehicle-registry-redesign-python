# Author     :  Omar Hamed Marie
# Reference  :  ArjanCodes
# Description:  cohesion-coupling-app-solutions
# Date       :  8 SEP 2022
# Version    :  V 1.0

import string
import random


class VehicleInfo:
    """
    Seperates Vehicle for vehicle info to reduce coupling
    """
    # Structure of variables to use | the data we will be dealing with in app
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        """Computing tax for the vehicle | Improves Cohesion"""
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        """prints vehicle information | Improves Cohesion"""
        print(f"Brand:       { self.brand         } ")
        print(f"Payable Tax: { self.compute_tax() } ")


class Vehicle:
    """
    Seperates Vehicle for vehicle info to reduce coupling
    """
    # Structure of variables to use | the data we will be dealing with in app 
    id: int
    license_plate: str
    info: VehicleInfo  # Refrence to the actual vehicle info 

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        """prints all vehicle needed data | Improves Cohesion"""
        print(f"ID: {self.id}")
        print(f"license_plate: {self.license_plate}")
        self.info.print()

class VehicleRegistry:
    """
    Vehicle Registry class is a Container for two helper methods
    """

    vehicle_info = {} # class attribute

    def add_vehicle_info(self, brand, catalogue_price, electric):
        """Function that adds vehicle information to an object vehicle_info"""
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    # Initialize to add some information to vehicle_info object
    def __init__(self):
        """Add some vehicle's information inside vehicle_info object when initializing"""
        self.add_vehicle_info("Volkswagen ID3" , 50000, True)
        self.add_vehicle_info("Tesla Model 3", 65000, True)
        self.add_vehicle_info("BMW 5", 70000, False)


    def generate_vehicle_id(self, length):
        """
        Generates an id for a vehicle

        @param length: integer
        @return: generated vehicle id
        """

        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        """
        Generate a license plate for the vehicle using the first two characters of the vehicle id
        
        @param id: the pre-generated id
        @return: license plate number
        """

        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


    def create_vehicle(self, brand):
        """
        Creates a vehicle inside VehicleRegistry class instead to increase cohesion and
        reduces coupling.

        @param brand: str
        @return: Vehicle obj
        """
        vehicle_id    = self.generate_vehicle_id(12) 
        license_plate = self.generate_vehicle_license(vehicle_id)
        # We still need the VehicleInfo to create new Vehicle | done in constructor
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])



class Application:
    """
    Main app gateway 
    
    Problems with this implementation:
        The method has very low cohesion (doing a lot of things)
        Also has a high coupling (depends on the registered vehicle class)
    """

    def register_vehicle(self, brand: string):
        """
        Creates an instance of registered vehicle generates id then uses it to create
        a license plate number and calculates the price of a car then computes the
        percetage and payable tax and prints out all the information..

        @param brand: brand name which is an integer
        @return: The created vehicle
        """

        # create a registry instance | This also creates some dummy vehicle info
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)       # create a new vehicle

# User code
app     = Application()
vehicle = app.register_vehicle("BMW 5")
vehicle.print()