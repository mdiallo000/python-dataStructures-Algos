class Solution:
    def randomizedString(s):
        count = Counter(s)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)
