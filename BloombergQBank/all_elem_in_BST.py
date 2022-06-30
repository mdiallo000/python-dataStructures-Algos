class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root1)
        inorder(root2)

        return res.sort()
