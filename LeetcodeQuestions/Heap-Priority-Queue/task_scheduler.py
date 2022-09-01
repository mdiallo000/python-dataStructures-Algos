from collections import deque
import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()

        while heap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
