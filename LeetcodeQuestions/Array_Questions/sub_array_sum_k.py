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
#  lesson learned
    #  my initial approach was to use a sum-variable, and a count, increment it with the values in the dictionary, whenever the the variable equal k than we coun increment the count. It was a sliding window technique

    #  The working solution involved a prefixSum
