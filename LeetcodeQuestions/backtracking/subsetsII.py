class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate(subsets, idx):

            if idx >= len(nums):
                res.append(subsets[:])
                return
            prev = -1
            for i in range(idx, len(nums)):
                if nums[i] == prev:
                    continue
