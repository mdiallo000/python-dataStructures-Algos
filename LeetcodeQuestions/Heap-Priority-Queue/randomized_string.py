from collections import deque
import heapq
import deque


class Solution:
    def randomizedString(s):
        count = Counter(s)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)

        q = deque()
