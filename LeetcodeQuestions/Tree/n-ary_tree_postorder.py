
class Solution:
    #     Given the root of an n-ary tree, return the post_order traversal of its nodes' values.

    # Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

    # Example 1:

    # Input: root = [1,null,3,2,4,null,5,6]
    # Output: [5,6,3,2,4,1]
    # Example 2:

    # Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    # Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
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
