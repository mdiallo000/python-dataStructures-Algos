class Solution:
    #  The ultimate goal is to use O(1) extra space
    #  If this requirement didnt exist then we could simply use a set and filter out the duplicate values
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):

            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1

    # Lessons Learned
        #  The naive solution generatd lots of extra complexity in terms of time and space
        #  This clever approach of using two pointer yields a time complexity O(n) and constant space
        #  When dealing with a sorted list with duplicates and the tasks requires us to deal with those duplicates then two pointer is the way to go
