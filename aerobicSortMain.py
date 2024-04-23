def aerobic_sort(arr):
    def partition(arr, low, high):
        pivot = arr[(low + high) // 2]
        left = low
        right = high
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

    def aerobic_recursive(arr, low, high):
        if low >= high:
            return
        left, right = partition(arr, low, high)
        aerobic_recursive(arr, low, right)
        aerobic_recursive(arr, left, high)

    aerobic_recursive(arr, 0, len(arr) - 1)
