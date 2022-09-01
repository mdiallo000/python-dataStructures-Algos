class Solution:
    def check(self, nums: List[int]) -> bool:
        # Determine wheter or not the array is sorted even after being rotated
        # The approach i took was to use pointers and partion the list in different havves and determine whether the sorting is consistent

        count = 0
        size = len(nums)
        for i in range(size):

            if nums[i] > nums[(i+1) % size]:
                count += 1

        return False if count > 1 else True

    def check(self, nums):

        b = sorted(nums)
        if b == nums:
            return True

        for i in range(len(nums)):

            a = nums.pop(0)
            nums.append(a)
            if nums == b:
                return True

        return False
