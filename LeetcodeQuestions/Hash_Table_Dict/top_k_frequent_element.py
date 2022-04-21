# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sample array we get [1,1,1,2,3,3,4,5,5,5]
        # goal is to bring back a K amount of the most freqent elements in the list
        # So first step is to map the element to how frequent it appears in the list

        myMap = {}
        myHeap = []

        for elem in nums:
            if elem not in myMap:
                myMap[elem] = 1
            else:
                myMap[elem] += 1
        #  Now that the array has been populated we can now use a short cut to return the largest frequencies determine by K
        # return heapq.nlargest(k, myMap.keys(), key=myMap.get())

        for elem, freq in myMap.items():
            if len(myHeap) < K:
                heapq.heappush(myHeap, [freq, elem])
            else:
                heapq.heappop(myHeap, [freq, elem])

        #  [[3,1],[3,5]]
        return [elem for value, key in myHeap]
