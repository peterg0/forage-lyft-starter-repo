from battery.battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(current_date, last_service_date):
    # Convert date strings to datetime objects
        current_date = datetime.strptime(current_date, '%Y-%m-%d')
        last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d')

        # Calculate the difference between the dates
        date_difference = current_date - last_service_date

        # Get the difference in years
        years_difference = date_difference.days / 365

        return years_difference > 2