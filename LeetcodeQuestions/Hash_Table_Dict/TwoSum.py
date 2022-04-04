# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# list3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#          l                       R
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, k in enumerate(nums, start=0):
            for i2, k2 in enumerate(nums[i+1:], start=0):
                if k + k2 == target:
                    return i, i2+i+1

    def Brute_version2(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
# Both of the above approaches are easy and utlize very inefficient approaches. We do find the locations of the two elements which add up to our target but in the worst case scenario it will take O(n^2) time complexity since we would have to compare each element of the array with every other element.

#  Below is a much more effiecient approach with a time Complexity of O(n)


class Answer:
    def TwoSumDict(self, nums: List[int], target: int) -> List[int]:
        # 1 Declare hash map
        myDict = {}
        # 2 Loop through the entire array
        for i in range(len(nums)-1):
            #  3 Save current element in curr
            curr = nums[i]
        # 4 find the difference bewtween curr and Target
            difference = target - curr
        # 5 Look if we already have the difference in our Map
            if difference in myDict:
                # 7 If we due then return the index of where we currently are and the location of where we found our difference
                return [i, myDict[difference]]
        # 8 If difference wasnt in Map then add curr into map and set its value to be its index
            else:
                myDict[curr] = i

# Space complexity is O(n) since we might have to map every element in our array.
