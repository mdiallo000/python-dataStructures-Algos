# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # for i in range(len(arr) - 1):
        #     curr_max = max(arr[i:])
        #     arr[i] = curr_max
        # arr[-1] = -1
        # return arr
        #  My initial approach worked on small inputs but yielded a time limit exception on larger inputs since it was an O(n^2) solution. Its because during each iteration we are looking at the entire remain array excluding our current position.
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr
        #  this approach was more acceptable since its linear in nature, rather than looking at the same elements over and over again we just keep track of the biggest number we have seen thus far on the right side of the list, reducing our overhead by a ton
