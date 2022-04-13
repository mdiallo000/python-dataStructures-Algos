
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     for j in range(i+1, len(nums)):
        #         elem_ahead = nums[j]
        #         if curr == elem_ahead:
        #             return curr

        mySet = set()

        for elem in nums:
            if elem not in mySet:
                mySet.add(elem)
            else:
                return elem
