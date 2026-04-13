import datetime
from app.services.util import room_not_available_error

class Room:
    def __init__(self, number: int, room_type: str, price_per_night: float):

        self.number = number
        self.type = room_type
        self.price_per_night = price_per_night
        self.availability = {}
        self.init_availability()
    def init_availability(self):
        start_date = datetime.date.today()
        for i in range(365):
            current_date = start_date + datetime.timedelta(days=i)
            self.availability[current_date] = None