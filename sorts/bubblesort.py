import unittest

def bubblesort(arr, sort="ascending"):
    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    while True:
        swapped = False

        # Start from first value in array
        for i in range(arr_len-1):
            if sort == "ascending":
                # Swap
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
            elif sort == "descending":
                # Swap
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
        
        if not swapped:
            break
    
    return arr

class TestBubbleSort(unittest.TestCase):
    def test_ascending_sort(self):
        arr = [4, 1, 2, 8, 3, 1]
        expected = [1, 1, 2, 3, 4, 8]
        self.assertEqual(bubblesort(arr), expected)

    def test_descending_sort(self):
        arr = [4, 1, 2, 8, 3, 1]
        expected = [8, 4, 3, 2, 1, 1]
        self.assertEqual(bubblesort(arr, sort="descending"), expected)

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(bubblesort(arr), expected)

    def test_single_element(self):
        arr = [5]
        expected = [5]
        self.assertEqual(bubblesort(arr), expected)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubblesort(arr), expected)

if __name__ == '__main__':
    unittest.main()