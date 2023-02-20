class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #  we want to return  the sub arrays of size k whos average greater than or equal to the threeshold
        #  since we are looking for sub-arrays we should either do a two pointer or a sliding window
        window = set()
        res = 0
        l = 0

        for r in range(len(arr)):
