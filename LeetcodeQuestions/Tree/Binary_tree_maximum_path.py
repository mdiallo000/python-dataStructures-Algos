# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            #  we are basically working bottom up, we drill down to the leaf nodes and begining calculating tha path sum running through the leaf nodes, once they find their path sum they will then send info to their caller as to which path from them generate the max path .
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            #  check to make sure its not negative value, if it is then send back a zero
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            #  THis calculates the maxPath running through this node plus its left and right sides
            res[0] = max(res[0], node.val + left_max + right_max)
            #  This information is returned to the caller and it allows it to know which sides yields the highest sum
            return node.val + max(left_max, right_max)

        dfs(root)

        return res[0]
# lessons learned:
    # This algorithm is attempting to do two things.
    # 1- Drill down all the way to the leaf nodes
    # 2- From there calculate the path sum running through the nodes left and right sides
    # 3-Always updated the pathSum value since we know that its possible for the max path to run through a node that isnt the root
    # 4 - Once we computed the path sum for a node we now need to send information to its caller as to where the maxPath is running through it Is it on the left? or right Side? This information will allow the caller to know which path is best
    # 5 - This approach yields a linear time complexity since we are only visiting a node once and there are no repeated visits
