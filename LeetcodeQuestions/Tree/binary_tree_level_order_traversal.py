# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #  the level order traversal of a binary is one of the essential traversal algorithms
        #  we will use a queue to simulate the level order traversal of the tree
        #  first we will add the root node into the queue
        #  once we began
