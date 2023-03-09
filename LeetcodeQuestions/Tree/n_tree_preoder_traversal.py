class Solution:
    def preOderNthTree(root):

        res = []

        def dfs(node):
            if not node:
                return

            res.append(node.val)
            for child in node.children:
                dfs(child)
