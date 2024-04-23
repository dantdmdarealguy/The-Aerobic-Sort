import random
import time
from aerobic_sort import aerobic_sort

class TestAerobicSort:
    @staticmethod
    def assert_sorted(arr):
        assert arr == sorted(arr), f"Array not sorted: {arr}"

    @staticmethod
    def test_random_input():
        arr = [random.randint(0, 100) for _ in range(100)]
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_small_arrays():
        for n in range(1, 11):
            arr = [random.randint(0, 100) for _ in range(n)]
            aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_large_arrays():
        arr = [random.randint(0, 1000000) for _ in range(1000000)]
        start_time = time.time()
        aerobic_sort(arr)
        end_time = time.time()
        TestAerobicSort.assert_sorted(arr)
        print(f"Sorted large array in {end_time - start_time:.2f} seconds.")

    @staticmethod
    def test_already_sorted():
        arr = list(range(1, 101))
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_reversed_arrays():
        arr = list(range(100, 0, -1))
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_nearly_sorted():
        arr = list(range(1, 101))
        arr[50], arr[51] = arr[51], arr[50]
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_duplicate_elements():
        arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(100)]
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_mixed_data():
        arr = [random.randint(-100, 100) for _ in range(100)]
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_empty_array():
        arr = []
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

    @staticmethod
    def test_single_element():
        arr = [42]
        aerobic_sort(arr)
        TestAerobicSort.assert_sorted(arr)

if __name__ == "__main__":
    test_suite = TestAerobicSort()
    test_suite.test_random_input()
    test_suite.test_small_arrays()
    test_suite.test_large_arrays()
    test_suite.test_already_sorted()
    test_suite.test_reversed_arrays()
    test_suite.test_nearly_sorted()
    test_suite.test_duplicate_elements()
    test_suite.test_mixed_data()
    test_suite.test_empty_array()
    test_suite.test_single_element()

    print("All tests passed.")
