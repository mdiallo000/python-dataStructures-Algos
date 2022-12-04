class Solution:
    def find132patternNaive(self, nums: List[int]) -> bool:
        # so all we need to determine is if there is a number that is both greather thab the previous and the
        #  i am thinking of maybe three loops, one on

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j] and nums[k] > nums[i]:
                        print(nums[i], nums[j], nums[k])
                        return True

        return False

    def find132pattern(nums):

        stack = []
        curMin = nums[0]
        for curr in nums:
            while stack and curr >= stack[-1][0]:
                stack.pop()
            if stack and curr > stack[-1][1]:
                return True
            stack.append([curr, curMin])
            curMin = min(curr, curMin)
        return False
