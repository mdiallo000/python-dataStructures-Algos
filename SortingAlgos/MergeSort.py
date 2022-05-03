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
