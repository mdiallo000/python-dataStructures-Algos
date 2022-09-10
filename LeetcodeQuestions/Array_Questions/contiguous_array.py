
def findMaxLength(nums):
    r = l = 0
    one_count = zero_count = 0

    while r < len(nums)-1:

        if nums[r] == 0:
            zero_count += 1
        if nums[r] == 1:
            one_count += 1
