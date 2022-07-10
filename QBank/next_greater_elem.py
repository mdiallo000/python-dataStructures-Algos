class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dataMap = {}
        stack = []

        for i in range(len(nums2)):
            n = nums2[i]
            while stack and stack[-1] < n:
                dataMap[stack.pop()] = n
                stack.append(n)

        while stack:
            dataMap[stack.pop()] = -1

        res = []

        for i in range(len(nums1)):

            res[i] = dataMap[nums1[i]]

        return res
