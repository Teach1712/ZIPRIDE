# =========================================================
# main.py (fixed)
# MENU DRIVEN ZIPRIDE SYSTEM
# =========================================================

from graph import Graph
from hash_table import PassengerHashTable, DriverHashTable, Passenger, Driver
from heap import MaxHeap, PickupRequest
from sorting import benchmark

# =========================================================
# GRAPH MODULE
# =========================================================
def run_graph_module():
    graph = Graph()

    # Add ≥8 nodes and ≥10 edges
    graph.add_road("CBD", "Airport", 15)
    graph.add_road("Airport", "IndustrialPark", 20)
    graph.add_road("CBD", "University", 10)
    graph.add_road("University", "ShoppingMall", 8)
    graph.add_road("ShoppingMall", "Hospital", 6)
    graph.add_road("Hospital", "IndustrialPark", 12)
    graph.add_road("CBD", "Stadium", 18)
    graph.add_road("Stadium", "Hospital", 14)
    graph.add_road("University", "Library", 5)
    graph.add_location("IsolatedPark")  # isolated node

    graph.print_graph()
    graph.bfs("CBD")
    graph.dfs_cycle("CBD")
    graph.dijkstra("CBD", "IndustrialPark")

# =========================================================
# HASH TABLE MODULE
# =========================================================
def run_hash_module():
    passenger_table = PassengerHashTable()
    driver_table = DriverHashTable()

    print("\n===== MODULE 2: HASH TABLE LOOKUP =====")

    # Insert passengers (20 records)
    for i in range(20):
        passenger = Passenger(101 + i, f"Passenger{i}", "CBD", (i % 5) + 1)
        passenger_table.insert(passenger)

    # Demonstrate collision explicitly
    p1 = Passenger(101, "CollisionA", "CBD", 2)
    p2 = Passenger(154, "CollisionB", "CBD", 3)  # same bucket as 101
    passenger_table.insert(p1)
    passenger_table.insert(p2)
    passenger_table.print_chain(101 % 53)

    # Search hit and miss
    passenger_table.search(101)   # hit
    passenger_table.search(9999)  # miss

    # Deletion followed by search
    passenger_table.delete(101)
    passenger_table.search(101)

    # Insert drivers
    for i in range(20):
        driver = Driver(201 + i, f"Driver{i}", "Airport", "Available")
        driver_table.insert(driver)

    driver_table.search(201)   # hit
    driver_table.search(9999)  # miss

    print("\n===== HASH TABLE MODULE COMPLETE =====")

# =========================================================
# HEAP MODULE
# =========================================================
def run_heap_module():
    heap = MaxHeap()
    graph = Graph()
    graph.add_road("CBD", "Airport", 15)
    graph.add_road("Airport", "IndustrialPark", 20)

    print("\n===== MODULE 3: HEAP PICKUP SCHEDULING =====")

    for i in range(5):
        passenger = Passenger(301 + i, f"Passenger{i}", "CBD", (i % 5) + 1)
        driver = Driver(401 + i, f"Driver{i}", "Airport", "Available")
        travel_time = graph.dijkstra(passenger.pickup_location, driver.current_location)
        request = PickupRequest(passenger, driver, travel_time)
        heap.insert(request)
        print(f"\nInserted Passenger: {passenger.passenger_id}")

    top = heap.peek()
    if top:
        print(f"\nHighest Priority Passenger: {top.passenger.passenger_id}")

    print("\nExtracting Requests:")
    for i in range(3):
        request = heap.extract_max()
        if request:
            print(f"Extracted Passenger: {request.passenger.passenger_id}")

    print("\n===== HEAP MODULE COMPLETE =====")

# =========================================================
# SORTING MODULE
# =========================================================
def run_sorting_module():
    benchmark()

# =========================================================
# FULL SYSTEM DEMO
# =========================================================
def run_full_demo():
    print("\n===== FULL SYSTEM DEMO =====")
    run_graph_module()
    run_hash_module()
    run_heap_module()
    run_sorting_module()
    print("\n===== FULL SYSTEM DEMO COMPLETE =====")

# =========================================================
# MENU
# =========================================================
def menu():
    while True:
        print("\n===== ZIPRIDE MENU =====")
        print("1. Graph Route Planning")
        print("2. Hash Table Lookup")
        print("3. Heap Pickup Scheduling")
        print("4. Sorting Pickup Records")
        print("5. Run Full System Demo")
        print("6. Exit")

        choice = input("\nEnter Option : ")

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
            print("\nExiting ZipRide System...")
            break
        else:
            print("\nInvalid Option")

# =========================================================
# RUN PROGRAM
# =========================================================
menu()
