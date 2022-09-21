class Solution:
    def findPeakElementLinear(self, nums: List[int]) -> int:

        #  the linear approach takes into consideration a couple scenarios in order to work

        for i in range(len(nums)):
            if i == len(nums)-1:
                break
            #  if the condition above isn't there then  we would get an index error

            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1
