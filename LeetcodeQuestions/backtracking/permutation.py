from itertools import permutations


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:

        res = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)
            for p in perm:
                p.append(n)
            res.extend(perm)
            nums.append(n)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(i, idx, arr):
            arr[i], arr[idx] = arr[idx], arr[i]

        res = []
        ans = []

        def generate(index):
            if index == len(nums):
                for i in range(len(nums)):
                    ans.append(nums[i])
                res.append[ans[:]]
                return

            for i in range(len(nums)):
                swap(i, index, nums)
                generate(index + 1)
                swap(i, index, nums)

        generate(0)
        return res
