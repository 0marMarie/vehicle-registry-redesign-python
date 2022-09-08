# Author     :  Omar Hamed Marie
# Reference  :  ArjanCodes
# Description:  cohesion-coupling-app-solutions
# Date       :  8 SEP 2022
# Version    :  V 1.0

import string
import random


class VehicleInfo:
    """
    Seperates Vehicle for vehicle info to decrease coupling
    """
    # Structure of variables to use | the data we will be dealing with in app
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric


class Vehicle:
    """
    Seperates Vehicle for vehicle info to decrease coupling
    """
    # Structure of variables to use | the data we will be dealing with in app
    id: int
    license_plate: str
    info: VehicleInfo  # Refrence to the actual vehicle info 

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info


class VehicleRegistry:
    """
    Vehicle Registry class is a Container for two helper methods
    """

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
        Creates a vehicle inside VehicleRegistry class instead to increase cohesion

        @param brand: str
        """
        vehicle_id    = self.generate_vehicle_id(12) 
        license_plate = self.generate_vehicle_license(vehicle_id)

        ## We still need the vehicle information to create new vehicle



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
        @return: None
        """

        # create a registry instance
        registry = VehicleRegistry()




        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")

app = Application()
app.register_vehicle("Volkswagen ID3")