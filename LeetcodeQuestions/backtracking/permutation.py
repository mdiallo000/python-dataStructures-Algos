from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        permutation = []
        freq = [False] * len(nums)

        def generate(permutation, freq):

            if len(permutation) >= len(nums):
                res.append(permutation.copy())
                return

            for i in range(nums):
                if i not in freq:
                    permutation.append(nums[i])
                    freq[i] = True
                    generate(permutation, freq)
                    permutation.pop(len(permutation)-1)
                    freq[i] = False

        generate(permutation, freq)
        return res
