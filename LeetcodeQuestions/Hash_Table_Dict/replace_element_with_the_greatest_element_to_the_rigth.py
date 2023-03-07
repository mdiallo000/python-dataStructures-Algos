# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # The goal of the problem is to take the original list, then go through it and make sure that for each element it is replaced with the greatest element to its right.
        # We also need to put a -1 at the last index of the list
        # [17,18,5,4,6,1] =>> [17,6,6,6,1,-1]
        # so if i had [14,5,6,8,2,4] then we should get [8,8,8,4,4,-1]
        # So what did i do step by step:
        #     i start at the end of the list
        #     next i save the element at that position as my current max and replace it with a negeative on
        #     I then go to my next number change it with whatever the current max is. Then check wheter this number is actually greater than my current max. I
        #     If it is i updated the new max
        #     We continue on until we solve the whole thing
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, temp)
        return arr
    #  This will be O(1) extra space and a linear algorithm
