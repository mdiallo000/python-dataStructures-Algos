class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        currMax = 0
        l, r = 0, 0
        total = 0
        while r <= len(nums)-1:
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            currMax = max(currMax, (r - l + 1))
            r += 1
        print(currMax)
        return currMax
