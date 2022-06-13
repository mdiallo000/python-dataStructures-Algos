class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        #  we need to sort the input array so that we can later apply logic that will prevent the inclusion of duplicates
        nums.sort()
        #  sorting will cost a time complexity of O(logN)

        def generate(subsets, idx):
            #  what is our base case?
            #  when our idx is the same as the len(nums) that means we have reached the end of our options
            if idx == len(nums):
                res.append(subsets[:])
                return
