from collections import defaultdict
from email.policy import default


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        cache = {0: 1}
        res = 0
        for num in nums:
            preSum += num

            if preSum - k in cache:
                res += cache[preSum - k]
            cache[preSum] = cache.get(preSum, 0) + 1
        return res
