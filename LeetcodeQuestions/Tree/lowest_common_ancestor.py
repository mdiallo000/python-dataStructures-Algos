

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.left)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.right)
        else:
            return root
