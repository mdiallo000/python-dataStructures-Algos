
def jump(nums):
    l, r = 0
    count = 0

    while r < len(nums)-1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest
        count += 1


nums = [2, 3, 1, 1, 4]
ans = jump(nums)
print(ans)
