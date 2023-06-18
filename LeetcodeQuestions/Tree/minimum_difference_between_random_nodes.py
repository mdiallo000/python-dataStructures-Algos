# Find the minimum difference between two nodes in the binary search tree
class Solution:

    def findMinDifference(root):
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)

        minVal = max(res)

        for i in range(1, len(res)):
            minVal = min(minVal, res[i] - res[i-1])
        return minVal
