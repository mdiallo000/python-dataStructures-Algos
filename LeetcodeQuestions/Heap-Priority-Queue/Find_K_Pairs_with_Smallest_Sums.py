
import heapq


def kSmallestPairs(nums1, nums2, k):

    heapq.heapify(nums1)
    heapq.heapify(nums2)
    res = []
    maxSum = 0

    while nums1 or nums2:

        for _ in range(k):
            one = heapq.heappop(nums1)
            second = heapq.heappop(nums2)
            maxSum = one + second
            minNUm = min(one, second)
            res.append([one, second])
    return res


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
ans = kSmallestPairs(nums1, nums2, k)
print(ans)
