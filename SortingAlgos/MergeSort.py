#  Divide and conquer algorithim that splits the original array into smaller managable pieces which will then be eaily merged back together in an ordered format. Hence why this algo has a Big O (logN).

# This Algo needs a helper function that will merge two arrays into one

def mergesort(arr):
    #  we only want to run this algo if there are more than one element
    if len(arr) > 1:
        #  first we partion the array into two halves, a left and a right
        left_side = arr[:len(arr)//2]
        right_side = arr[len(arr)//2:]
        #  now we recursively run the function which will do the dividing for us

        mergesort(left_side)
        mergesort(right_side)
        # once the partitioning is complete we can begin on merging into a sorted collection
        #  i will keep track of the left most position of our left_side array
        i = 0
        #  j will keep track of the left most position of our right_side array
        j = 0
        #  k will keep track of the left most position of our ending sorted array
        k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
        # now we can insert any remaing elements into the sorted array

        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

    return arr


test = [1, 4, 57, 12, 1, 8, 76, 45, 12, 86, 35, 21]
print(mergesort(test))
