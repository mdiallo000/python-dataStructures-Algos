# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        Map = {}
        for i in range(len(arr) - 1):
            curr_max = max(arr[i:])
            Map[i] = curr_max
        arr[-1] = -1

        for key, val in
