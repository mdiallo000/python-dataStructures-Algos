from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #  This will be a level order traversal but now we will do it in a zizag form after each level

        res = []

        q = deque()
        q.append(root)
        left_right = True
        while q:
            size = len(q)
            level = []
            for _
