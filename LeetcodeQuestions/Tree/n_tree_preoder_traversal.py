class TreeNode:
    def __init__(self, val, children) -> None:
        self.val = val
        self.children = children


class Solution:
    def preOderNthTree(root):

        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return root
