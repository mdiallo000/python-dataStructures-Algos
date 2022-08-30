class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        end = -1
        total = 0
        maxLength = 0
        while start < n:
            while end + 1 < n and total + arr[end + 1] <= k:
                total += arr[end += 1]

            if total == k:
                maxLength = max(maxLength, (end - start + 1))

            total -= arr[start]
            start++

        return maxLength
