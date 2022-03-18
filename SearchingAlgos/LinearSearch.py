# ** Linear Search Sorting Algorithm will search through a collection of data and return the location of the target of interest

def linear_search(arr, target):
    # We get the size of the array to allow us to loop through it
    arrSize = len(arr)-1

    # Next we loop through the array and as we encounter each element we check to see if it matches our Target
    for elem in range(arrSize):
        if arr[elem] == target:
            return elem
    # If we dont encounter the element that means it isnt present so we return...
    return -1

# Linear Search has a big of 0(n) if n represents the number of items in the list. Meaning we will have to examine each element in the array until we encounter the target element.
# Worst Case we loop through the entire list and dont find the element at all


print(linear_search([4, 56, 72, 12, 56, 45], 12))
