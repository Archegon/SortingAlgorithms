import unittest

def _partition(arr, low, high, sort="ascending"):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if sort is "ascending":
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j] , arr[i]
        elif sort is "descending":
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j] , arr[i]
                

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quicksort(arr, low=0, high=None, sort="ascending"):
    if len(arr) == 1:
        return arr
    if high is None:
        high = len(arr)-1
    if low < high:
        pi = _partition(arr, low, high, sort=sort)

        quicksort(arr, low, pi-1, sort=sort)
        quicksort(arr, pi+1, high, sort=sort)
    return arr

class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        arr = [10, 7, 8, 9, 1, 5]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [1, 5, 7, 8, 9, 10])

    def test_quicksort_empty(self):
        arr = []
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [])

    def test_quicksort_descending(self):
        arr = [10, 7, 8, 9, 1, 5]
        sorted_arr = quicksort(arr, sort="descending")
        self.assertEqual(sorted_arr, [10, 9, 8, 7, 5, 1])

if __name__ == '__main__':
    unittest.main()