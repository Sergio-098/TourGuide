class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.saved_trips = []  # List of Trip objects

    def save_trip(self, trip):
        self.saved_trips.append(trip)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "saved_trips": [trip.to_dict() for trip in self.saved_trips]
        }

