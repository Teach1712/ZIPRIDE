# =========================================================
# hash_table.py
# =========================================================
# Author: Richa
# Description:
# Module 2 - Hash Based Passenger and Driver Lookup
# Uses:
# - Chaining with Linked Lists
# - Modulo Hash Function
# - NumPy Arrays instead of Python Lists
# - No dict, hashmap, tuples, heapq, sort, index, find
# =========================================================

import numpy as np

TABLE_SIZE = 53


# =========================================================
# PASSENGER CLASS
# =========================================================

class Passenger:

    def __init__(
            self,
            passenger_id,
            name,
            pickup_location,
            membership_tier):

        self.passenger_id = passenger_id
        self.name = name
        self.pickup_location = pickup_location
        self.membership_tier = membership_tier


# =========================================================
# DRIVER CLASS
# =========================================================

class Driver:

    def __init__(
            self,
            driver_id,
            name,
            current_location,
            availability_status):

        self.driver_id = driver_id
        self.name = name
        self.current_location = current_location
        self.availability_status = availability_status


# =========================================================
# LINKED LIST NODE
# =========================================================

class Node:

    def __init__(
            self,
            key,
            data):

        self.key = key
        self.data = data
        self.next = None


# =========================================================
# PASSENGER HASH TABLE
# =========================================================

class PassengerHashTable:

    def __init__(self):

        self.size = TABLE_SIZE

        self.table = np.empty(
            TABLE_SIZE,
            dtype=object
        )

        for i in range(TABLE_SIZE):

            self.table[i] = None

        self.count = 0

    # -----------------------------------------------------

    def hash_function(self, key):

        return key % self.size

    # -----------------------------------------------------

    def insert(self, passenger):

        if not isinstance(
                passenger.passenger_id,
                int):

            print(
                "Passenger ID must be integer"
            )
            return

        if passenger.membership_tier < 1 or \
           passenger.membership_tier > 5:

            print(
                "Invalid membership tier: REJECTED"
            )
            return

        if passenger.name == "":

            print(
                "Empty passenger name: REJECTED"
            )
            return

        index = self.hash_function(
            passenger.passenger_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == \
                    passenger.passenger_id:

                print(
                    "Duplicate passenger ID: REJECTED"
                )
                return

            current = current.next

        new_node = Node(
            passenger.passenger_id,
            passenger
        )

        new_node.next = self.table[index]

        self.table[index] = new_node

        self.count += 1

        if new_node.next is not None:

            print(
                "Collision detected at bucket",
                index
            )

        if self.count % 10 == 0:

            print(
                "Load factor after",
                self.count,
                "inserts:",
                round(
                    self.load_factor(),
                    2
                )
            )

    # -----------------------------------------------------

    def search(self, passenger_id):

        index = self.hash_function(
            passenger_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == passenger_id:

                print(
                    "Search Passenger",
                    passenger_id,
                    ": FOUND"
                )

                return current.data

            current = current.next

        print(
            "Search Passenger",
            passenger_id,
            ": NOT FOUND"
        )

        return None

    # -----------------------------------------------------

    def delete(self, passenger_id):

        index = self.hash_function(
            passenger_id
        )

        current = self.table[index]

        previous = None

        while current is not None:

            if current.key == passenger_id:

                if previous is None:

                    self.table[index] = \
                        current.next

                else:

                    previous.next = \
                        current.next

                self.count -= 1

                print(
                    "Delete Passenger",
                    passenger_id,
                    ": SUCCESS"
                )

                return

            previous = current
            current = current.next

        print(
            "Delete Passenger",
            passenger_id,
            ": KEY NOT FOUND"
        )

    # -----------------------------------------------------

    def load_factor(self):

        return self.count / self.size

    # -----------------------------------------------------

    def print_chain(self, index):

        current = self.table[index]

        print(
            "Bucket",
            index,
            "Chain:"
        )

        while current is not None:

            print(
                current.key,
                end=""
            )

            if current.next is not None:

                print(
                    " -> ",
                    end=""
                )

            current = current.next

        print()

    # -----------------------------------------------------

    def display(self):

        print(
            "\n===== PASSENGER HASH TABLE ====="
        )

        for i in range(self.size):

            if self.table[i] is not None:

                print(
                    "Bucket",
                    i,
                    ":",
                    end=" "
                )

                current = self.table[i]

                while current is not None:

                    print(
                        current.key,
                        end=" "
                    )

                    current = current.next

                print()


# =========================================================
# DRIVER HASH TABLE
# =========================================================

class DriverHashTable:

    def __init__(self):

        self.size = TABLE_SIZE

        self.table = np.empty(
            TABLE_SIZE,
            dtype=object
        )

        for i in range(TABLE_SIZE):

            self.table[i] = None

        self.count = 0

    # -----------------------------------------------------

    def hash_function(self, key):

        return key % self.size

    # -----------------------------------------------------

    def insert(self, driver):

        if not isinstance(
                driver.driver_id,
                int):

            print(
                "Driver ID must be integer"
            )
            return

        if driver.name == "":

            print(
                "Empty driver name: REJECTED"
            )
            return

        if driver.availability_status != \
                "Available" and \
           driver.availability_status != \
                "Busy" and \
           driver.availability_status != \
                "Offline":

            print(
                "Invalid driver status: REJECTED"
            )
            return

        index = self.hash_function(
            driver.driver_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == driver.driver_id:

                print(
                    "Duplicate driver ID: REJECTED"
                )
                return

            current = current.next

        new_node = Node(
            driver.driver_id,
            driver
        )

        new_node.next = self.table[index]

        self.table[index] = new_node

        self.count += 1

        if new_node.next is not None:

            print(
                "Collision detected at bucket",
                index
            )

        if self.count % 10 == 0:

            print(
                "Load factor after",
                self.count,
                "inserts:",
                round(
                    self.load_factor(),
                    2
                )
            )

    # -----------------------------------------------------

    def search(self, driver_id):

        index = self.hash_function(
            driver_id
        )

        current = self.table[index]

        while current is not None:

            if current.key == driver_id:

                print(
                    "Search Driver",
                    driver_id,
                    ": FOUND"
                )

                return current.data

            current = current.next

        print(
            "Search Driver",
            driver_id,
            ": NOT FOUND"
        )

        return None

    # -----------------------------------------------------

    def delete(self, driver_id):

        index = self.hash_function(
            driver_id
        )

        current = self.table[index]

        previous = None

        while current is not None:

            if current.key == driver_id:

                if previous is None:

                    self.table[index] = \
                        current.next

                else:

                    previous.next = \
                        current.next

                self.count -= 1

                print(
                    "Delete Driver",
                    driver_id,
                    ": SUCCESS"
                )

                return

            previous = current
            current = current.next

        print(
            "Delete Driver",
            driver_id,
            ": KEY NOT FOUND"
        )

    # -----------------------------------------------------

    def load_factor(self):

        return self.count / self.size

    # -----------------------------------------------------

    def display(self):

        print(
            "\n===== DRIVER HASH TABLE ====="
        )

        for i in range(self.size):

            if self.table[i] is not None:

                print(
                    "Bucket",
                    i,
                    ":",
                    end=" "
                )

                current = self.table[i]

                while current is not None:

                    print(
                        current.key,
                        end=" "
                    )

                    current = current.next

                print()
