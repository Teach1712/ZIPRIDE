# =========================================================
# main.py
# =========================================================

import numpy as np

from graph import Graph
from hash_table import (
    PassengerHashTable,
    DriverHashTable,
    Passenger,
    Driver
)

from heap import (
    MaxHeap,
    PickupRequest
)

from sorting import benchmark


INF = 999999


# =========================================================
# MODULE 1
# =========================================================

def run_graph_module():

    graph = Graph()

    graph.add_road(
        "CBD",
        "Airport",
        15
    )

    graph.add_road(
        "Airport",
        "IndustrialPark",
        20
    )

    graph.add_road(
        "CBD",
        "University",
        10
    )

    graph.add_road(
        "University",
        "ShoppingMall",
        8
    )

    graph.add_road(
        "ShoppingMall",
        "Hospital",
        6
    )

    graph.add_road(
        "Hospital",
        "IndustrialPark",
        12
    )

    graph.add_road(
        "CBD",
        "Stadium",
        18
    )

    graph.add_road(
        "Stadium",
        "Hospital",
        14
    )

    graph.add_road(
        "University",
        "Library",
        5
    )

    graph.add_road(
        "ShoppingMall",
        "Daycare",
        7
    )

    graph.add_location(
        "IsolatedPark"
    )

    graph.print_graph()

    graph.bfs(
        "CBD"
    )

    graph.dfs_cycle()

    graph.dijkstra(
        "CBD",
        "IndustrialPark"
    )


# =========================================================
# MODULE 2
# =========================================================

def run_hash_module():

    passenger_table = \
        PassengerHashTable()

    driver_table = \
        DriverHashTable()

    print(
        "\n===== MODULE 2:"
        " HASH TABLE LOOKUP ====="
    )

    for i in range(20):

        passenger = Passenger(
            101 + i,
            "Passenger" + str(i),
            "CBD",
            (i % 5) + 1
        )

        passenger_table.insert(
            passenger
        )

    passenger_table.search(
        101
    )

    passenger_table.search(
        9999
    )

    passenger_table.delete(
        101
    )

    passenger_table.search(
        101
    )

    for i in range(20):

        driver = Driver(
            201 + i,
            "Driver" + str(i),
            "Airport",
            "Available"
        )

        driver_table.insert(
            driver
        )

    driver_table.search(
        201
    )

    driver_table.search(
        9999
    )

    driver_table.delete(
        201
    )

    driver_table.search(
        201
    )

    print(
        "\n===== HASH TABLE "
        "MODULE COMPLETE ====="
    )


# =========================================================
# MODULE 3
# =========================================================

def run_heap_module():

    heap = MaxHeap()

    graph = Graph()

    graph.add_road(
        "CBD",
        "Airport",
        15
    )

    graph.add_road(
        "Airport",
        "IndustrialPark",
        20
    )

    graph.add_road(
        "CBD",
        "Hospital",
        25
    )

    print(
        "\n===== MODULE 3:"
        " HEAP PICKUP "
        "SCHEDULING ====="
    )

    for i in range(10):

        passenger = Passenger(
            301 + i,
            "Passenger" + str(i),
            "CBD",
            (i % 5) + 1
        )

        driver = Driver(
            401 + i,
            "Driver" + str(i),
            "Airport",
            "Available"
        )

        travel_time = \
            graph.dijkstra(
                passenger.pickup_location,
                driver.current_location
            )

        request = PickupRequest(
            passenger,
            driver,
            travel_time
        )

        heap.insert(
            request
        )

        print(
            "\nInserted Passenger:",
            passenger.passenger_id
        )

    # -------------------------------------------------
    # Driver comparison
    # -------------------------------------------------

    passenger = Passenger(
        999,
        "PassengerX",
        "CBD",
        2
    )

    drivers = np.empty(
        3,
        dtype=object
    )

    drivers[0] = Driver(
        601,
        "DriverA",
        "Airport",
        "Available"
    )

    drivers[1] = Driver(
        602,
        "DriverB",
        "Hospital",
        "Available"
    )

    drivers[2] = Driver(
        603,
        "DriverC",
        "IndustrialPark",
        "Available"
    )

    best_driver = None

    best_time = INF

    for i in range(3):

        current_driver = \
            drivers[i]

        travel_time = \
            graph.dijkstra(
                passenger.pickup_location,
                current_driver.current_location
            )

        print(
            "Driver",
            current_driver.driver_id,
            "travel time:",
            travel_time
        )

        if travel_time < best_time:

            best_time = \
                travel_time

            best_driver = \
                current_driver

    print(
        "Best driver:",
        best_driver.driver_id,
        "Time:",
        best_time
    )

    request = PickupRequest(
        passenger,
        best_driver,
        best_time
    )

    heap.insert(
        request
    )

    top = heap.peek()

    if top is not None:

        print(
            "\nHighest Priority "
            "Passenger:",
            top.passenger.passenger_id
        )

    print(
        "\nExtracting Requests:"
    )

    for i in range(5):

        request = \
            heap.extract_max()

        if request is not None:

            print(
                "Extracted Passenger:",
                request.passenger.passenger_id
            )

    print(
        "\n===== HEAP MODULE "
        "COMPLETE ====="
    )


# =========================================================
# MODULE 4
# =========================================================

def run_sorting_module():

    benchmark()


# =========================================================
# FULL DEMO
# =========================================================

def run_full_demo():

    print(
        "\n===== FULL SYSTEM "
        "DEMO ====="
    )

    run_graph_module()

    run_hash_module()

    run_heap_module()

    run_sorting_module()

    print(
        "\n===== FULL SYSTEM "
        "DEMO COMPLETE ====="
    )


# =========================================================
# MENU
# =========================================================

def menu():

    running = True

    while running:

        print(
            "\n===== ZIPRIDE MENU ====="
        )

        print(
            "1. Graph Route Planning"
        )

        print(
            "2. Hash Table Lookup"
        )

        print(
            "3. Heap Pickup Scheduling"
        )

        print(
            "4. Sorting Pickup Records"
        )

        print(
            "5. Run Full System Demo"
        )

        print(
            "6. Exit"
        )

        choice = input(
            "\nEnter Option : "
        )

        if choice == "1":

            run_graph_module()

        elif choice == "2":

            run_hash_module()

        elif choice == "3":

            run_heap_module()

        elif choice == "4":

            run_sorting_module()

        elif choice == "5":

            run_full_demo()

        elif choice == "6":

            print(
                "\nExiting ZipRide "
                "Dispatch System..."
            )

            running = False

        else:

            print(
                "\nInvalid Option"
            )


# =========================================================
# PROGRAM START
# =========================================================

menu()
