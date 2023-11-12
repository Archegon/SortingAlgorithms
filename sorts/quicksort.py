def _partition(arr, low, high, ascending=True):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if ascending:
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j] , arr[i]
        else:
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j] , arr[i]
                

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quicksort(arr, low=0, high=None, ascending=True):
    if len(arr) == 1:
        return arr
    if high is None:
        high = len(arr)-1
    if low < high:
        pi = _partition(arr, low, high, ascending=ascending)

        quicksort(arr, low, pi-1, ascending)
        quicksort(arr, pi+1, high, ascending)
    return arr