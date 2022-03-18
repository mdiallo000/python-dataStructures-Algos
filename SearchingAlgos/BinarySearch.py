# Binary search is a higly efficient searching Algo that will find a target witing a array. The array must be sorted or the algo will not work since it relies on comparing the elements

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid-1

    return -1


print(binary_search([4, 5, 75, 82, 92, 105, 230], 105))
