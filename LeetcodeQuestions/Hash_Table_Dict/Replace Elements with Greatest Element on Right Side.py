# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # for i in range(len(arr) - 1):
        #     curr_max = max(arr[i:])
        #     arr[i] = curr_max
        # arr[-1] = -1
        # return arr

        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
