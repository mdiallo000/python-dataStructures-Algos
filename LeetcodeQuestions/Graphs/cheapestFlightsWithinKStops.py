from cmath import inf


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #  we could use digjstra's algo but that would require us to change it and complexity wouldnt be good as if we used Bellmond ford
        prices = [float(inf)] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[::]

            for sr, ds, pr in flights:
                if prices[src] == float(inf):
                    continue
                if prices[sr] + pr < tmp[ds]:
                    tmp[ds] = prices[sr] + pr
            prices = tmp
        return -1 if float(inf) == prices[dst] else prices[dst]
