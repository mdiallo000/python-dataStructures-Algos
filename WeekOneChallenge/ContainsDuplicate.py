from typing import Set


class Solution:
    def containsDuplicate_BruteForce(self, nums: List[int]) -> bool:
        mySet = Set()

        for elem in nums:
            if elem not in mySet:
                mySet.add(elem)
            else:
                return True
        return False
