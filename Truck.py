class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        """Return a string representation of the truck."""
        return (f"Capacity: {self.capacity}, Speed: {self.speed} mph, Load: {self.load}, "
                f"Packages: {self.packages}, Mileage: {self.mileage:.2f} miles, "
                f"Address: {self.address}, Depart Time: {self.depart_time}")

