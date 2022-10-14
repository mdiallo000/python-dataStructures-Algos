

def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
