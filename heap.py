# =========================================================
# heap.py (fixed)
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
        # Correct priority formula: (6 - M) + 1000/T
        self.priority = (6 - passenger.membership_tier) + (1000 / travel_time if travel_time > 0 else 0)

# =========================================================
# MAX HEAP CLASS
# =========================================================
class MaxHeap:
    def __init__(self):
        self.heap = [None] * MAX_HEAP
        self.size = 0

    # =====================================================
    # INSERT
    # =====================================================
    def insert(self, request):
        if request is None:
            print("Invalid request: cannot insert")
            return

        self.heap[self.size] = request
        index = self.size

        # Heapify up
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

        self.size += 1
        self.print_heap()  # print after every insert

    # =====================================================
    # EXTRACT MAX
    # =====================================================
    def extract_max(self):
        if self.size == 0:
            print("Heap Empty")
            return None

        root = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap[self.size] = None

        index = 0
        # Heapify down
        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            largest = index

            if left < self.size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < self.size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

        self.print_heap()  # print after every extraction
        return root

    # =====================================================
    # PEEK
    # =====================================================
    def peek(self):
        return None if self.size == 0 else self.heap[0]

    # =====================================================
    # PRINT HEAP
    # =====================================================
    def print_heap(self):
        print("\nHeap State:")
        if self.size == 0:
            print("Heap Empty")
            return
        for i in range(self.size):
            request = self.heap[i]
            print(
                f"[Passenger: {request.passenger.passenger_id} | "
                f"Driver: {request.driver.driver_id} | "
                f"Priority: {round(request.priority, 2)}]"
            )
