# =========================================================
# heap.py (NumPy version, no dicts/tuples)
# =========================================================

import numpy as np

MAX_HEAP = 100

# =========================================================
# PICKUP REQUEST CLASS
# =========================================================
class PickupRequest:
    def __init__(self, passenger, driver, travel_time):
        self.passenger = passenger
        self.driver = driver
        # Priority formula: (6 - M) + 1000/T
        self.priority = (6 - passenger.membership_tier) + (1000 / travel_time if travel_time > 0 else 0)

# =========================================================
# MAX HEAP CLASS
# =========================================================
class MaxHeap:
    def __init__(self):
        # Use NumPy arrays for storage
        self.passenger_ids = np.zeros(MAX_HEAP, dtype=int)
        self.driver_ids = np.zeros(MAX_HEAP, dtype=int)
        self.priorities = np.zeros(MAX_HEAP, dtype=float)
        self.requests = np.empty(MAX_HEAP, dtype=object)
        self.size = 0

    # =====================================================
    # INSERT
    # =====================================================
    def insert(self, request):
        if request is None:
            print("Invalid request: cannot insert")
            return

        # Store request data in NumPy arrays
        self.passenger_ids[self.size] = request.passenger.passenger_id
        self.driver_ids[self.size] = request.driver.driver_id
        self.priorities[self.size] = request.priority
        self.requests[self.size] = request

        index = self.size
        # Heapify up
        while index > 0:
            parent = (index - 1) // 2
            if self.priorities[index] > self.priorities[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

        self.size += 1
        self.print_heap()

    # =====================================================
    # EXTRACT MAX
    # =====================================================
    def extract_max(self):
        if self.size == 0:
            print("Heap Empty")
            return None

        root = self.requests[0]
        self.size -= 1

        # Move last element to root
        self._swap(0, self.size)

        index = 0
        # Heapify down
        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            largest = index

            if left < self.size and self.priorities[left] > self.priorities[largest]:
                largest = left
            if right < self.size and self.priorities[right] > self.priorities[largest]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

        self.print_heap()
        return root

    # =====================================================
    # PEEK
    # =====================================================
    def peek(self):
        return None if self.size == 0 else self.requests[0]

    # =====================================================
    # PRINT HEAP
    # =====================================================
    def print_heap(self):
        print("\nHeap State:")
        if self.size == 0:
            print("Heap Empty")
            return
        for i in range(self.size):
            print(
                f"[Passenger: {self.passenger_ids[i]} | "
                f"Driver: {self.driver_ids[i]} | "
                f"Priority: {round(self.priorities[i], 2)}]"
            )

    # =====================================================
    # SWAP HELPER
    # =====================================================
    def _swap(self, i, j):
        # Swap across all arrays
        self.passenger_ids[i], self.passenger_ids[j] = self.passenger_ids[j], self.passenger_ids[i]
        self.driver_ids[i], self.driver_ids[j] = self.driver_ids[j], self.driver_ids[i]
        self.priorities[i], self.priorities[j] = self.priorities[j], self.priorities[i]
        self.requests[i], self.requests[j] = self.requests[j], self.requests[i]
