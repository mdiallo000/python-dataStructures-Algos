class TreeNode:
    def __init__(self, val, children) -> None:
        self.val = val
        self.children = children

# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)


# Example 1:


# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:


# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
class Solution:
    def preOderNthTree(root):
        #  first off lets define preOrder tree traversal
        #  we will visit the current node
        #  next we will visit the left side, then we will visit the right side
        # the problem is different from other binary search type questions since this one has a childrens field rather than the typical left, right arrangement
        #  i think each nodes will need a list where we can store its children nodes as well.
        #  okay now how do i go about traversing the tree and add each  node and its children
        #  so lets start from the root
        #  i add the current node in the list then i add a list for its children and then inside that list i will append all the child nodes.
        #  next we will loop through this list and do the same thing over and over
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return root
