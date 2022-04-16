

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or q:
            return None

        list1 = []
        list2 = []

        list1.append(p.val)
        list2.append(q.val)
        self.isSameTree(p.left)
        self.isSameTree(p.righ)
        self.isSameTree(q.left)
        self.isSameTree(q.righ)
        return True if list1 == list2 else False
