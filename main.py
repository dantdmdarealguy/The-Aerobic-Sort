import random
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return arr[mid]

def partition(arr, low, high):
    pivot = median_of_three(arr, low, high)
    left, right = low, high
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left, right

def sort_partition(arr, low, high):
    if high - low < 20:
        insertion_sort(arr, low, high)
        return
    if low < high:
        left, right = partition(arr, low, high)
        sort_partition(arr, low, right)
        sort_partition(arr, left, high)

def parallel_aerobic_sort(arr):
    num_processes = 4
    chunk_size = len(arr) // num_processes
    futures = []

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        for i in range(num_processes):
            low = i * chunk_size
            high = (i + 1) * chunk_size - 1 if i < num_processes - 1 else len(arr) - 1
            futures.append(executor.submit(sort_partition, arr, low, high))

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing partition: {e}")

    merge_sorted_chunks(arr, num_processes)

def merge_sorted_chunks(arr, num_chunks):
    chunk_size = len(arr) // num_chunks
    sorted_arr = []
    
    for i in range(num_chunks):
        low = i * chunk_size
        high = (i + 1) * chunk_size - 1 if i < num_chunks - 1 else len(arr) - 1
        sorted_arr.extend(arr[low:high + 1])
    
    arr[:] = sorted(sorted_arr)

class TestAerobicSort:
    @staticmethod
    def assert_sorted(arr):
        assert arr == sorted(arr), f"Array not sorted: {arr}"

    @staticmethod
    def test_empty_array():
        arr = []
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_single_element():
        arr = [42]
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_two_elements_sorted():
        arr = [1, 2]
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_two_elements_unsorted():
        arr = [2, 1]
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_identical_elements():
        arr = [5] * 1000
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_sorted_array():
        arr = list(range(1, 101))
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_reverse_sorted_array():
        arr = list(range(100, 0, -1))
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_almost_sorted_array():
        arr = list(range(1, 101))
        arr[50], arr[51] = arr[51], arr[50]
        parallel_aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_large_arrays():
        for size in [10000, 100000, 500000, 1000000]:
            arr = [random.randint(0, 1000000) for _ in range(size)]
            start_time = time.time()
            parallel_aerobic_sort(arr)
            end_time = time.time()
            TestAerobicSort.assert_sorted(arr)
            print(f"Sorted array of size {size} in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    test_suite = TestAerobicSort()
    test_suite.test_empty_array()
    test_suite.test_single_element()
    test_suite.test_two_elements_sorted()
    test_suite.test_two_elements_unsorted()
    test_suite.test_identical_elements()
    test_suite.test_sorted_array()
    test_suite.test_reverse_sorted_array()
    test_suite.test_almost_sorted_array()
    test_suite.test_large_arrays()

    print("All tests passed.")
