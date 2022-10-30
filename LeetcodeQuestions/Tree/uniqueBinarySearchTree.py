class Solution:

    def numTrees(self, n: int) -> int:

        numTree = [1] * n + 1

        for nodes in range(2, n+1):
            total = 0
