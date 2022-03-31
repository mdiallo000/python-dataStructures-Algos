
def selection_sort(arr: int):
    for i in range(1, len(arr)):
        key = arr[i+1]
        j = i-1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
