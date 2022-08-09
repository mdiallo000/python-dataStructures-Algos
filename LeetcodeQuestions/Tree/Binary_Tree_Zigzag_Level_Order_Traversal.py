from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #  This will be a level order traversal but now we will do it in a zizag form after each level

        res = []

        level = deque()

        left_right = True
        node_queue = deque([root, None])
        while node_queue:
            curr = node_queue.popleft()
            if curr:
                if left_right:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
            else:
