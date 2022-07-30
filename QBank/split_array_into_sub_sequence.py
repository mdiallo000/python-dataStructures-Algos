from collections import defaultdict
from email.policy import default


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        Frequency = Counter(nums)
        end = defaultdict()

        for n in nums:
            # first check is to establish if we still have this number left in our frequency maping

            if Frequency[n]:
