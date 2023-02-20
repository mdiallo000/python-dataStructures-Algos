class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #  we want to return  the sub arrays of size k whos average greater than or equal to the threeshold
        #  since we are looking for sub-arrays we should either do a two pointer or a sliding window
        window = set()
        res = 0
        l, r = 0, k - 1
        # while r < len(arr):
        #     while l <= r:
        #         window += arr[l]
        #         l +=1
        #     average =  window//k
        #     if average >= threshold:
        #         res +=1
        #     r += k - 1
        #     window = 0
        # return res
