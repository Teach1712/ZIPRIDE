# 🚖 ZipRide Dispatch System

A menu-driven Python project simulating a ride dispatch system with graph-based route planning, hash table lookups, heap scheduling, and sorting benchmarks.  
This project demonstrates core data structures and algorithms integrated into a single dispatch workflow.

---

## 📌 Features

### [Graph Module]
- Represents city locations as nodes and roads as weighted edges.
- Supports **BFS traversal**, **DFS cycle detection**, and **Dijkstra shortest path**.
- Includes ≥8 nodes, ≥10 edges, and an isolated node for robustness testing.

### [Hash Table Module]
- Stores passengers and drivers using **separate chaining**.
- Demonstrates **collisions**, **load factor tracking**, **search hits/misses**, and **deletion followed by search**.
- Validates membership tiers and driver statuses.

### [Heap Module]
- Implements a **max heap** for scheduling pickup requests.
- Priority formula:  
  

\[
  \text{Priority} = (6 - M) + \frac{1000}{T}
  \]

  
  where `M` = membership tier, `T` = travel time from Dijkstra.
- Prints heap state after every insert and extraction.
- Handles edge cases (no drivers, invalid input).

### [Sorting Module]
- Implements **merge sort** and **quick sort** manually (no built-ins).
- Benchmarks on **random**, **nearly-sorted**, and **reversed** datasets.
- Tracks **operation counts** and execution times.

### [Main Menu]
- Interactive menu to run each module individually or full demo.
- Full demo integrates all modules:
  - Passengers/drivers stored in hash tables.
  - Dijkstra computes travel times.
  - Heap schedules pickups by priority.
  - Sorting benchmarks pickup records.

---

## 🛠 Requirements
- Python 3.9+ (tested on Python 3.13)
- NumPy (for random dataset generation)

Install dependencies:
```bash
pip install numpy
