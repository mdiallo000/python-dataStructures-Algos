
from curses import window


def findMaxLength(nums):
    r = l = 0
    one_count = zero_count = 0
    window = 0
    while r < len(nums)-1:

        if nums[r] == 0:
            zero_count += 1
        if nums[r] == 1:
            one_count += 1
        if one_count > 1 and zero_count > 1 and zero_count == one_count:
            window = max(window, )
