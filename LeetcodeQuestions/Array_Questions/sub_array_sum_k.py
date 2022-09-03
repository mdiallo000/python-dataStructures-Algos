from collections import defaultdict
from email.policy import default


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        cache = defaultdict(int)

        for num in nums:
            preSum += num

            if preSum
