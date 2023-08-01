from car import Car
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # You should implement the specific logic for the Capulet Engine and Spindler Battery here
        engine = CapuletEngine(current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(last_service_date, engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # You should implement the specific logic for the Willoughby Engine and Spindler Battery here
        engine = WilloughbyEngine(current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(last_service_date, engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        # You should implement the specific logic for the Sternman Engine here
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(last_service_date, engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # You should implement the specific logic for the Willoughby Engine and Nubbin Battery here
        engine = WilloughbyEngine(current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(last_service_date, engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # You should implement the specific logic for the Capulet Engine and Nubbin Battery here
        engine = CapuletEngine(current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(last_service_date, engine, battery)
