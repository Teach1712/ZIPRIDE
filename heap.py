# =========================================================
# heap.py
# =========================================================

import numpy as np

MAX_HEAP = 100


# =========================================================
# HEAP NODE
# =========================================================

class HeapNode:

    def __init__(
            self,
            passenger,
            driver,
            priority):

        self.passenger = passenger
        self.driver = driver
        self.priority = priority


# =========================================================
# PICKUP REQUEST
# =========================================================

class PickupRequest:

    def __init__(
            self,
            passenger,
            driver,
            travel_time):

        self.passenger = passenger
        self.driver = driver

        if travel_time > 0:

            self.priority = \
                (6 -
                 passenger.membership_tier) + \
                (1000 / travel_time)

        else:

            self.priority = 0


# =========================================================
# MAX HEAP
# =========================================================

class MaxHeap:

    def __init__(self):

        self.heap = np.empty(
            MAX_HEAP,
            dtype=object
        )

        self.size = 0

    # -----------------------------------------------------

    def insert(self, request):

        if request is None:

            print(
                "Invalid request"
            )

            return

        node = HeapNode(
            request.passenger,
            request.driver,
            request.priority
        )

        self.heap[self.size] = node

        current = self.size

        self.size += 1

        self.heapify_up(current)

        self.print_heap()

    # -----------------------------------------------------

    def heapify_up(
            self,
            current):

        while current > 0:

            parent = \
                (current - 1) // 2

            if self.heap[current].priority > \
               self.heap[parent].priority:

                self.swap(
                    current,
                    parent
                )

                current = parent

            else:

                break

    # -----------------------------------------------------

    def extract_max(self):

        if self.size == 0:

            print(
                "Heap Empty"
            )

            return None

        root = self.heap[0]

        self.size -= 1

        self.heap[0] = \
            self.heap[self.size]

        self.heap[self.size] = None

        self.heapify_down(0)

        self.print_heap()

        return root

    # -----------------------------------------------------

    def heapify_down(
            self,
            current):

        while True:

            left = \
                (2 * current) + 1

            right = \
                (2 * current) + 2

            largest = current

            if left < self.size:

                if self.heap[left].priority > \
                   self.heap[largest].priority:

                    largest = left

            if right < self.size:

                if self.heap[right].priority > \
                   self.heap[largest].priority:

                    largest = right

            if largest != current:

                self.swap(
                    current,
                    largest
                )

                current = largest

            else:

                break

    # -----------------------------------------------------

    def peek(self):

        if self.size == 0:

            return None

        return self.heap[0]

    # -----------------------------------------------------

    def swap(
            self,
            i,
            j):

        temp = self.heap[i]

        self.heap[i] = \
            self.heap[j]

        self.heap[j] = temp

    # -----------------------------------------------------

    def print_heap(self):

        print(
            "\n===== HEAP STATE ====="
        )

        if self.size == 0:

            print(
                "Heap Empty"
            )

            return

        for i in range(self.size):

            node = self.heap[i]

            print(
                "Passenger:",
                node.passenger.passenger_id,
                "| Driver:",
                node.driver.driver_id,
                "| Priority:",
                round(
                    node.priority,
                    2
                )
            )
