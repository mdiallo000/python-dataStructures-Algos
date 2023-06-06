# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections


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

        res = []
        q = deque()
        q.append(root)
