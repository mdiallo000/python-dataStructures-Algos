# ** Linear Search Sorting Algorithm will search through a collection of data and return the location of the target of interest

def linear_search(arr, target):
    # We get the size of the array to allow us to loop through it
    arrSize = len(arr)-1

    # Next we loop through the array and as we encounter each element we check to see if it matches our Target
    for elem in range(n):
        if arr[elem] == target:
            return elem
    # If we dont encounter the element that means it isnt present so we return...
    return -1
