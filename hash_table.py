import numpy as np
TABLE_SIZE = 53

class Passenger:
    def __init__(self, passenger_id, name, pickup_location, membership_tier):
        self.passenger_id = passenger_id
        self.name = name
        self.pickup_location = pickup_location
        self.membership_tier = membership_tier

class Driver:
    def __init__(self, driver_id, name, current_location, availability_status):
        self.driver_id = driver_id
        self.name = name
        self.current_location = current_location
        self.availability_status = availability_status

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class PassengerHashTable:
    def __init__(self):
        self.size = TABLE_SIZE
        self.table = [None] * TABLE_SIZE
        self.count = 0

    def hash_function(self, key):
        return key % self.size

    def insert(self, passenger):
        if passenger.membership_tier < 1 or passenger.membership_tier > 5:
            print("Invalid membership tier: REJECTED")
            return
        if passenger.name == "":
            print("Empty passenger name: REJECTED")
            return

        index = self.hash_function(passenger.passenger_id)
        current = self.table[index]

        while current is not None:
            if current.key == passenger.passenger_id:
                print("Duplicate passenger ID: REJECTED")
                return
            current = current.next

        node = Node(passenger.passenger_id, passenger)
        node.next = self.table[index]
        self.table[index] = node
        self.count += 1

        # Print collision state
        if node.next is not None:
            print(f"Collision detected at bucket {index}! Chain updated.")

        # Print load factor every 10 inserts
        if self.count % 10 == 0:
            print(f"Load factor after {self.count} inserts: {self.load_factor():.2f}")

    def search(self, passenger_id):
        index = self.hash_function(passenger_id)
        current = self.table[index]
        while current is not None:
            if current.key == passenger_id:
                print(f"Search hit: Passenger {passenger_id} FOUND")
                return current.data
            current = current.next
        print(f"Search miss: Passenger {passenger_id} NOT FOUND")
        return None

    def delete(self, passenger_id):
        index = self.hash_function(passenger_id)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.key == passenger_id:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                print(f"Delete Passenger {passenger_id}: SUCCESS")
                return
            previous = current
            current = current.next
        print(f"Delete Passenger {passenger_id}: KEY NOT FOUND")

    def load_factor(self):
        return self.count / self.size

    def print_chain(self, index):
        """Utility to print chain state at a bucket"""
        current = self.table[index]
        chain = []
        while current:
            chain.append(str(current.key))
            current = current.next
        print(f"Bucket {index} chain: {' -> '.join(chain) if chain else 'Empty'}")

class DriverHashTable:
    def __init__(self):
        self.size = TABLE_SIZE
        self.table = [None] * TABLE_SIZE
        self.count = 0
    def hash_function(self, key):
        return key % self.size
    def insert(self, driver):
        valid_status = ["Available", "Busy", "Offline"]
        if driver.availability_status not in valid_status:
            print("Invalid driver status: REJECTED")
            return
        index = self.hash_function(driver.driver_id)
        current = self.table[index]
        while current is not None:
            if current.key == driver.driver_id:
                print("Duplicate driver ID: REJECTED")
                return
            current = current.next
        node = Node(driver.driver_id, driver)
        node.next = self.table[index]
        self.table[index] = node
        self.count += 1
        if node.next is not None:
            print(f"Collision detected at bucket {index}! Chain updated.")
        if self.count % 10 == 0:
            print(f"Load factor after {self.count} inserts: {self.load_factor():.2f}")
    def search(self, driver_id):
        index = self.hash_function(driver_id)
        current = self.table[index]
        while current is not None:
            if current.key == driver_id:
                print(f"Search hit: Driver {driver_id} FOUND")
                return current.data
            current = current.next
        print(f"Search miss: Driver {driver_id} NOT FOUND")
        return None
    def delete(self, driver_id):
        index = self.hash_function(driver_id)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.key == driver_id:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                print(f"Delete Driver {driver_id}: SUCCESS")
                return
            previous = current
            current = current.next
        print(f"Delete Driver {driver_id}: KEY NOT FOUND")
    def load_factor(self):
        return self.count / self.size
