# selection sort involves selecting a min value at the start of our list and then subsquently comparing any subsequent values to the min, if a new min value is found then we uopdate.

mylist = [1, 456, 71, 5, 67, 20, 35, 16]


def selection_sort(arr):

    for i in range(0, len(arr)):

        minval = i

        for j in range(i+1, len(arr)):
            # the next line reads, if the element ahead is greater than the min val then make it the new minval
            if arr[j] < arr[minval]:
                minval = j

            # when we find the min val in this window then we can perform the swap
        if minval != i:
            arr[minval], arr[i] = arr[i], arr[minval]

    return arr


print(selection_sort(mylist))
