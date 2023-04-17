
def selection_sort(arr: int):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [45, 78, 12, 66, 79, 2, 31, 9, 45, 72, 100]

selection_sort(arr)
