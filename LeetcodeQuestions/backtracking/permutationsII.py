from collections import Counter


class Solution:
    def permutationsDuplicates(self, nums):
        output = []
        count = Counter(nums)

        def backtrack(perms):
            if len(perms) == len(nums):
                output.append()
                return
