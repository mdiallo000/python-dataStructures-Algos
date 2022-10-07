import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ""
        wrd = [(-a, "a"), (-b, "b"), (-c, 'c')]

        for count, char in wrd:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            # there are a couple of conditions one needs to keep track of, we will continually prioritize the char with the higest count as long as we dont have 3 of them in a row
            c1, char1 = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == char1:
                #  if this condition is true it means that we have 2 consecutive chars that are the same, so we need to ignore this one and instead use the second most frequent character
                c2, char2 = heapq.heappop(maxHeap)

                if c2:
                    res += char2
                    c2 += 1
                    heapq.heappush(maxHeap, (c2, char2))
            else:
                res += char
                c1 += 1
            if c1:
                heapq.heappush(maxHeap, (c1, char1))
