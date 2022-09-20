
import heapq as hq


def kSmallestPairs(nums1, nums2, k):

    heap = []
    result = []

    for i in range(min(k, len(nums1))):
        hq.heappush(heap, (nums1[i] + nums2[0], i, 0))
    print(heap)
    for _ in range(k):
        if not heap:
            break

        s, idx1, idx2 = hq.heappop(heap)
        result.append([nums1[idx1], nums2[idx2]])

        if idx2 < len(nums2) - 1:
            hq.heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))

    return result


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
ans = kSmallestPairs(nums1, nums2, k)
print(ans)
