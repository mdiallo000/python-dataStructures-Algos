class Solution:

    def next_greater(self, nums1, nums2):

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
