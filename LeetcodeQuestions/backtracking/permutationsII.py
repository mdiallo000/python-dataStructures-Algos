class Solution:
    def permutationsDuplicates(self, nums):
        output = []

        def backtrack(index, perms):
