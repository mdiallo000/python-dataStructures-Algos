class Solution:
    def permutationsDuplicates(self, nums):
        output = []

        def backtrack(index, perms):
            if len(perms) == len(nums):
                output.append(perms[::])
