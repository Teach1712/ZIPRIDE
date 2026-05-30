# =========================================================
# sorting.py
# =========================================================

import numpy as np
import time

MERGE_OPS = 0
QUICK_OPS = 0


# =========================================================
# MERGE SORT
# =========================================================

def merge_sort(arr, size):

    if size <= 1:

        return arr

    mid = size // 2

    left = np.empty(
        mid,
        dtype=int
    )

    right = np.empty(
        size - mid,
        dtype=int
    )

    for i in range(mid):

        left[i] = arr[i]

    for i in range(
            mid,
            size):

        right[i - mid] = arr[i]

    left = merge_sort(
        left,
        mid
    )

    right = merge_sort(
        right,
        size - mid
    )

    return merge(
        left,
        mid,
        right,
        size - mid
    )


# =========================================================
# MERGE
# =========================================================

def merge(
        left,
        left_size,
        right,
        right_size):

    global MERGE_OPS

    result = np.empty(
        left_size +
        right_size,
        dtype=int
    )

    i = 0
    j = 0
    k = 0

    while i < left_size and \
          j < right_size:

        MERGE_OPS += 1

        if left[i] <= right[j]:

            result[k] = left[i]

            i += 1

        else:

            result[k] = right[j]

            j += 1

        k += 1

    while i < left_size:

        result[k] = left[i]

        i += 1
        k += 1

    while j < right_size:

        result[k] = right[j]

        j += 1
        k += 1

    return result


# =========================================================
# QUICK SORT
# =========================================================

def quick_sort(
        arr,
        low,
        high):

    if low < high:

        pivot = partition(
            arr,
            low,
            high
        )

        quick_sort(
            arr,
            low,
            pivot - 1
        )

        quick_sort(
            arr,
            pivot + 1,
            high
        )


# =========================================================
# PARTITION
# =========================================================

def partition(
        arr,
        low,
        high):

    global QUICK_OPS

    pivot = arr[high]

    i = low - 1

    for j in range(
            low,
            high):

        QUICK_OPS += 1

        if arr[j] <= pivot:

            i += 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1


# =========================================================
# PRINT ARRAY
# =========================================================

def print_array(
        arr,
        size):

    for i in range(size):

        print(
            arr[i],
            end=" "
        )

    print()


# =========================================================
# BENCHMARK
# =========================================================

def benchmark():

    global MERGE_OPS
    global QUICK_OPS

    print(
        "\n===== MODULE 4: "
        "SORTING PICKUP RECORDS ====="
    )

    print(
        "\nSorting Field:"
        " EstimatedPickupTime"
    )

    # ------------------------------------
    # Correctness Test
    # ------------------------------------

    values = np.array(
        [45, 12, 78, 23, 9],
        dtype=int
    )

    print(
        "\nCorrectness Test:"
    )

    print(
        "Original:"
    )

    print_array(
        values,
        5
    )

    MERGE_OPS = 0
    QUICK_OPS = 0

    merge_result = merge_sort(
        values.copy(),
        5
    )

    quick_result = values.copy()

    quick_sort(
        quick_result,
        0,
        4
    )

    print(
        "\nMerge Sort:"
    )

    print_array(
        merge_result,
        5
    )

    print(
        "Quick Sort:"
    )

    print_array(
        quick_result,
        5
    )

    print(
        "Merge Ops:",
        MERGE_OPS
    )

    print(
        "Quick Ops:",
        QUICK_OPS
    )

    # ------------------------------------
    # Dataset Testing
    # ------------------------------------

    sizes = np.array(
        [100, 500, 1000],
        dtype=int
    )

    for s in range(3):

        size = sizes[s]

        print(
            "\nDataset Size:",
            size
        )

        # Random Data

        data = np.random.randint(
            1,
            1000,
            size
        )

        MERGE_OPS = 0
        QUICK_OPS = 0

        start = time.time()

        merge_sort(
            data.copy(),
            size
        )

        merge_time = \
            time.time() - start

        quick_data = data.copy()

        start = time.time()

        quick_sort(
            quick_data,
            0,
            size - 1
        )

        quick_time = \
            time.time() - start

        print(
            "Random:",
            round(
                merge_time,
                6
            ),
            round(
                quick_time,
                6
            )
        )

        print(
            "Merge Ops:",
            MERGE_OPS
        )

        print(
            "Quick Ops:",
            QUICK_OPS
        )

    print(
        "\n===== SORTING MODULE COMPLETE ====="
    )
