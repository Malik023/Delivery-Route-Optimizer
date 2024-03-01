import datetime
class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None


    # Learned how to do these comments here https://www.w3schools.com/python/python_comments.asp
    def __str__(self):
        """Return a string representation of the package."""
        return (f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zipcode}, "
                f"{self.Deadline_time}, {self.weight}Kg, Delivered at: {self.delivery_time}, Status: {self.status}")

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At Hub"
        if self.ID == 9:  # Added Edge case that will change the address for package 9 to the correct address once it's been received
                if convert_timedelta > datetime.timedelta(hours=10, minutes=20):
                    self.address = "410 S State St"
                    self.zipcode = "84111"
                else:
                    self.address = "300 State St"
                    self.zipcode = "84103"



