class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ""
        wrd = [(-a, "a"), (-b, "b"), (-c, 'c')]
