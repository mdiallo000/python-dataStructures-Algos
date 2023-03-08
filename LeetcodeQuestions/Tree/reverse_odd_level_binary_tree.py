# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #  the problem requires us to reverse the levels whenever the level is odd
        #  since its a binary tree and we need to do the operations based on the levels, we should consider bfs as the primary tool to achieve this
        #  general speaking we will perform the general bfs algo routine with a small twist for every instance the level we are on happens to be odd.
        #  we can keep track of an integer variable that will let us know were we are
        #  this variable will begin at 0 and it will be incremented after we pass each level.
        #  whenever level % 2 != 0 than its odd and the reversal needs to take place.
        #  i am thinking it may be easier to actually perform the reversal when we are at an even level, since then we will have access to that roots children nodes and their values can changed right away

        #  initial approach did not work for trees that have more than four leaf nodes
        #  an alternative is to use an extra list that will store the values of
        q = deque()
        level_values = []
        q.append(root)
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                    # if this level is even than lets store the values of its children in a list
                    if level % 2 == 0:
                        level_values.append(node.left.val)
                        level_values.append(node.right.val)
                if level % 2 != 0:
                    node.val = level_values.pop()
            level += 1
        # return root of tree
        return root
