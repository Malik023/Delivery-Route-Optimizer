
import csv
import datetime
import Truck
from builtins import ValueError

from HashTable import CreateHashMap
from Package import Package

# Read the file of distance information
with open("CSV/Distance.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file of address information
with open("CSV/Address.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)

# Read the file of package information
with open("CSV/Package.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)


# Create package objects from the CSV package file
# Load package objects into the hash table: package_hash_table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # Create New Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # Insert data into hash table
            package_hash_table.insert(pID, p)


# Method for finding distance between two addresses
def distance_between_address(x_value, y_value):
    distance = CSV_Distance[x_value][y_value]
    if distance == '':
        distance = CSV_Distance[y_value][x_value]

    return float(distance)


# Method to get address number from string literal of address
def get_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Create truck object truck1
truck1 = Truck.Truck(16, 18, None, [13, 14, 15, 16, 19, 20, 29, 31], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck.Truck(16, 18, None, [38, 3, 36, 18, 6, 32, 28, 25, 2, 8, 10, 12, 21, 23, 37, 40], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=10))

# Create truck object truck3
truck3 = Truck.Truck(16, 18, None, [1, 4, 5, 7, 9, 11, 17, 22, 24, 26, 27, 30, 33, 34, 35, 39], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=10, minutes=30))

# Create hash table
package_hash_table = CreateHashMap()

# Load packages into hash table
load_package_data("CSV/Package.csv", package_hash_table)


# Method for ordering packages on a given truck using the nearest neighbor algo
# This method also calculates the distance a given truck drives once the packages are sorted
def deliver_packages(truck):
    # Place all packages into array of not delivered
    not_delivered = []
    for packageID in truck.packages:
        package = package_hash_table.lookup(packageID)
        not_delivered.append(package)
    # Clear the package list of a given truck so the packages can be placed back into the truck in the order
    # of the nearest neighbor
    truck.packages.clear()

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(not_delivered) > 0:
        next_address = 2000
        next_package = None
        for package in not_delivered:
            if distance_between_address(get_address(truck.address), get_address(package.address)) <= next_address:
                next_address = distance_between_address(get_address(truck.address), get_address(package.address))
                next_package = package
        # Adds next closest package to the truck package list
        truck.packages.append(next_package.ID)
        # Removes the same package from the not_delivered list
        not_delivered.remove(next_package)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.mileage += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


# Put the trucks through the loading process
deliver_packages(truck1)
deliver_packages(truck2)
# Make sure that truck 3 does not leave until either of the first two trucks are finished
# delivering the packages
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3)


class Main:

    # Here I initialized methods to use within Main when i start up the program to make the code cleaner
    @staticmethod
    def welcome_message(total_mileage):
        print("Welcome to Western Governors University Parcel Service (WGUPS)")
        print("The total mileage for the route is:", total_mileage)

    @staticmethod
    def get_user_input():
        return input("To start, please type 'check' to check package status (Type 'quit' to exit): ").lower()

    @staticmethod
    def get_user_time():
        user_time = input("Please enter the time to check status of package(s) (HH:MM:SS): ")
        try:
            return datetime.datetime.strptime(user_time, "%H:%M:%S")
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS.")
            return None

    @staticmethod
    def get_user_package_option():
        return input("To view the status of an individual package, type 'single'. For all packages, type 'all': ").lower()

    @staticmethod
    def get_user_package_id():
        return input("Enter the numeric package ID: ")

    @staticmethod
    def display_package_status(package):
        print(package)

    @staticmethod
    def display_invalid_input():
        print("Invalid input. Closing program.")

    @staticmethod
    def display_package_invalid():
        print("Invalid package ID. Closing program.")

    @staticmethod
    def display_time_invalid():
        print("Invalid time format. Closing program.")

    @staticmethod
    def goodbye_message():
        print("Thank you for using WGUPS. Have a great day!")

def main():
    # calculate total mileage
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

    # Display welcome message and total mileage
    Main.welcome_message(total_mileage)

    # Get user input
    text = Main.get_user_input()

    # Handle user input
    if text == "check":
        user_time = Main.get_user_time()
        if user_time:
            package_option = Main.get_user_package_option()
            if package_option == "single":
                package_id = Main.get_user_package_id()
                # display individual package status
                try:
                    package = package_hash_table.lookup(int(package_id))
                    Main.display_package_status(package)
                except ValueError:
                    Main.display_package_invalid()
            elif package_option == "all":
                # display status of all packages
                for package_id in range(1, 41):
                    try:
                        package = package_hash_table.lookup(package_id)
                        Main.display_package_status(package)
                    except ValueError:
                        Main.display_package_invalid()
            else:
                Main.display_invalid_input()
        else:
            Main.display_time_invalid()
    elif text == "quit":
        Main.goodbye_message()
    else:
        Main.display_invalid_input()

if __name__ == "__main__":
    main()
