# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myHashMap = {}
        store = []
        if len(nums) == 1:
            return store.append(nums)
        for elem in nums:
            if elem not in myHashMap:
                myHashMap[elem] = 1
            else:
                myHashMap[elem] += 1
        for key in myHashMap:
            if myHashMap[key] > 1:
                store.append(key)
        return store
