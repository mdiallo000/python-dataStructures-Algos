class Solution:
    def findPeakElementLinear(self, nums: List[int]) -> int:

        #  the linear approach takes into consideration a couple scenarios in order to work

        #  case one:
        #  if the list is in descending order such as [5,4,3,2,1] than we know that continuing the loop will not solve the problem and we should just return the first index
        # case two:
        #  if the list is in ascending oder then we should [1,2,3,4,5] also return the first index since i criteria will not be met

        #  case three:
        # if we have this situtation then

        for i in range(len(nums)):
            if i == len(nums)-1:
                break
            #  if the condition above isn't there then  we would get an index error

            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1

    def findPeakElementLinearLogrithmic(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l <= r:

            mid = r + l // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
