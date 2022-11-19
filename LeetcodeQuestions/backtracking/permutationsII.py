from collections import Counter


class Solution:
    def permutationsDuplicates(self, nums):
        output = []
        count = Counter(nums)

        def backtrack(perms):
            if len(perms) == len(nums):
                output.append(perms[::])
                return

            for n in count:
                if count[n] > 0:
                    perms.append(n)
                    count[n] -= 1
                    backtrack(perms)
                    perms.pop()
                    count[n] += 1
        backtrack([])
        return output
