# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# The approach to take is to put each element in the list as a key inside an dictionary, if the element isnt in the list than give it a key of 1, if it is already in the dictionary that means its a duplicate so we give it a  key of two.
# All that remains is to return the Key that has a value of 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myDict = {}
        for elem in nums:
            if elem not in myDict:
                myDict[elem] = 1
            else:
                myDict[elem] = 2
        for k, v in myDict.items():
            if v == 1:
                return k
