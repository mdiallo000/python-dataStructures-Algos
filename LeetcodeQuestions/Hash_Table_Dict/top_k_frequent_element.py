# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myHashMap = {}

        for elem in nums:
            if elem not in myHashMap:
                myHashMap[elem] = 1
            else:
                myHashMap[elem] += 1
