from collections import Counter


#  this will be a place where i will practice

def bubbleSort(nums):
    #  bubble sort is a naive sorting algorithm that will sort the element in an array
    #  the time complexity that will result for performing the computation will be O(n^2)

    for r in range(len(nums)):

        for j in range(r-1):
            print(r, j)
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
        print(nums)
    return nums


lst = [14, 7, 8, 12, 68, 45, 12, 32, 89, 41, 23]

# res = bubbleSort(lst)


def MergeSort(nums):
    #  we will continue dividing until there is one element left in the array
    if len(nums) > 1:

        right = nums[len(nums)//2:]
        left = nums[:len(nums)//2]

        MergeSort(left)
        MergeSort(right)

        #  outside of this function
        l = 0
        j = 0
        r = 0

        while r < len(right) and l < len(left):
            if left[l] < right[r]:

                nums[j] = left[l]
                l += 1
            else:
                nums[j] = right[r]
                r += 1
            j += 1
        #  now we add the remaining elements in the array
        while l < len(left):

            nums[j] = left[l]
            l += 1
            j += 1

        while r < len(right):
            nums[j] = right[r]
            r += 1
            j += 1
    return nums


def Merge(left, right):
    l = 0
    j = 0
    r = 0

    while r < len(right) and l < len(left):
        if left[l] < right[r]:

            nums[j] = left[l]
            l += 1
        else:
            nums[j] = right[r]
            r += 1
        j += 1
    #  now we add the remaining elements in the array
    while l < len(left):

        nums[j] = left[l]
        l += 1
        j += 1

    while r < len(right):
        nums[j] = right[r]
        r += 1
        j += 1


def selectionSort(nums):
    #  selection sort is an naive sorting algorithm that looks for the minimum value and places it in front of the array
    # print(res)
    for i in range(len(nums)):

        minval = i
        for j in range(1, len(nums)):

            if nums[j] < nums[minval]:
                minval = j

        tmp = nums[minval]
        nums[minval] = minval[i]
        minval[i] = tmp
