# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int):
        res = []

        def dfs(start, arr):
            if len(arr) == k:
                res.append(arr[::])
                return

            for i in range(start, n+1):
                arr.append(i)
                dfs(i+1, arr)
                arr.pop()

        dfs(1, [])
        return res
        # time complexity will be K* n^k
