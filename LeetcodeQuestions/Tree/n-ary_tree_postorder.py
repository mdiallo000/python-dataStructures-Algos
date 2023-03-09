
class Solution:

    def postOrder(root):
        #  okay we did a similar problem just now.
        #  post_order traversal requires us to visit the last node after every other node has been visited
        #  so the root should be last
        #  after we visited all the children then we began adding the node into the result list
        res = []
        res = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            res.append(node.val)
        dfs(root)
        return res
