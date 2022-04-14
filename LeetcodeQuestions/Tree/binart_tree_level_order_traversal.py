# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque(root)

        while queue is not None:
            #  measure the length of our queue currently, we will use this to loop through the elements at the current level only
