
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resulting_arr = []
        # Sort the array and now we can apply the same technique we used in 2sumTwo
        nums.sort()
#
        for cur_index, curr in enumerate(nums):
            #       now we can make sure that we arent looking at duplicates since its sorted, a duplacte means if the curr elem is the same as its next
            if cur_index > 0 and curr == nums[index - 1]:
                continue

            # Now that we have skipped the duplicate we can began using our Two pointer method
            l, r = cur_index + 1, len(nums)-1
            while l < r:
                sum3 = curr + nums[l] + nums[r]
                if sum3 < 0:
                    l += 1
                elif sum3
