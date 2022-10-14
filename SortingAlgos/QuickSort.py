

def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s
