class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #  we want to return  the sub arrays of size k whos average greater than or equal to the threeshold
        #  since we are looking for sub-arrays we should either do a two pointer or a sliding window
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res
