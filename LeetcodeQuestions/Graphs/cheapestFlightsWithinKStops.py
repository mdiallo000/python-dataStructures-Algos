class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float(inf)] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[::]
