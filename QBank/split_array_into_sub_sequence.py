from collections import defaultdict
from email.policy import default


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        Frequency = Counter(nums)
        end = defaultdict()

        for n in nums:
            # first check is to establish if we still have this number left in our frequency maping

            if Frequency[n]:
                Frequency[n] -= 1

                #  Now if this number can be merged into the previous than we can
                if end[n - 1]:
                    end[n] += 1
                    end[n - 1] -= 1

                elif Frequency[n+1] and Frequency[n+2]:
                    Frequency[n+1]
