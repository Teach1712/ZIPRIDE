# =========================================================
# sorting.py (fixed)
# =========================================================

import numpy as np
import time

# Global counters
merge_ops = 0
quick_ops = 0

def merge_sort(arr):
    global merge_ops
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global merge_ops
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        merge_ops += 1  # comparison
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    global quick_ops
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for x in arr:
        quick_ops += 1  # comparison
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

def benchmark():
    print("\n===== MODULE 4: SORTING PICKUP RECORDS =====")
    print("\nSorting Field: EstimatedPickupTime T ascending")

    # Correctness Test
    values = [45, 12, 78, 23, 9]
    print("\nCorrectness Test:")
    print("Original T values:", values)
    global merge_ops, quick_ops
    merge_ops = quick_ops = 0
    merge_result = merge_sort(values)
    quick_result = quick_sort(values)
    print("Merge sort result:", merge_result)
    print("Quick sort result:", quick_result)
    print("Merge ops:", merge_ops, "Quick ops:", quick_ops)
    print("Correctness check:", "PASSED" if merge_result == quick_result else "FAILED")

    sizes = [100, 500, 1000]
    for size in sizes:
        print("\nDataset Size:", size)
        print("Condition | Merge Sort Time | Quick Sort Time | Merge Ops | Quick Ops")

        # Random
        data = np.random.randint(1, 1000, size).tolist()
        merge_ops = quick_ops = 0
        start = time.time(); merge_sort(data); merge_time = time.time() - start
        start = time.time(); quick_sort(data); quick_time = time.time() - start
        print("Random   |", round(merge_time, 6), "|", round(quick_time, 6), "|", merge_ops, "|", quick_ops)

        # Nearly Sorted
        data = list(range(size))
        # Introduce small disorder
        if size > 10:
            data[5], data[6] = data[6], data[5]
        merge_ops = quick_ops = 0
        start = time.time(); merge_sort(data); merge_time = time.time() - start
        start = time.time(); quick_sort(data); quick_time = time.time() - start
        print("NearlySorted |", round(merge_time, 6), "|", round(quick_time, 6), "|", merge_ops, "|", quick_ops)

        # Reversed
        data = list(range(size, 0, -1))
        merge_ops = quick_ops = 0
        start = time.time(); merge_sort(data); merge_time = time.time() - start
        start = time.time(); quick_sort(data); quick_time = time.time() - start
        print("Reversed |", round(merge_time, 6), "|", round(quick_time, 6), "|", merge_ops, "|", quick_ops)

    print("\n===== SORTING MODULE COMPLETE =====")
