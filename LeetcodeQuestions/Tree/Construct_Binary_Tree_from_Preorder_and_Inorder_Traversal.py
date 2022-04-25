# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder and not inorder:
            return None

        # Lets find the root in our Preodered list since the first element [0] is the root

        root = TreeNode(preorder[0])
        # Now lets find all the elments to the left of our root and to the right of it

        mid = inorder.index(preorder[0])

        #  now we can reconstruct the tree starting from the root, we will built left side first
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
