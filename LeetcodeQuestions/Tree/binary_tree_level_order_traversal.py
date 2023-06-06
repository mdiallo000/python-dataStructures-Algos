# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #  the level order traversal of a binary is one of the essential traversal algorithms
        #  we will use a queue to simulate the level order traversal of the tree
        #  first we will add the root node into the queue
        #  we will run the traversal as long as there are items inside of the queue
        #  we will iterate over the queue and pop nodes out
        # we will initialize an levels array that will be filled up with every node in the tree
        #  once we pop a node out will then check whether the node has a left and right child node. If it does we add the children node inside of the queue
        #  the queue essentially keeps the order of the nodes based  on their levels
        # after we are done iterating over that level we will then add the node into the level list
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            for _ in range(size):

                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            # after we exit the loop we will then make a final check to make sure we are only adding none empty levels into our result array
            if level:
                res.append(level)

        return res
