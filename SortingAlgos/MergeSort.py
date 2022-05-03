#  Divide and conquer algorithim that splits the original array into smaller managable pieces which will then be eaily merged back together in an ordered format. Hence why this algo has a Big O (logN).

# This Algo needs a helper function that will merge two arrays into one

def mergesort(arr):

    if len(arr) > 1:
