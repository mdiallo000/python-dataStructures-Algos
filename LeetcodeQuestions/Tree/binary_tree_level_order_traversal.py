# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            #  measure the length of our queue currently, we will use this to loop through the elements at the current level only
            lenght_queue = len(queue)
            # at each level we will store the nodes into a list
            levels = []
            for i in range(lenght_queue):
                #  now we store the node currently at the front of the queue by poping it out
                curr_node = queue.popleft()
            # Once we pop it out we can store it into the levels array and then we will add its left and child node into the queue
                if curr_node is not None:
                    levels.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            # now we can append the levels into our results array
            if levels:
                result.append(levels)
        return result
