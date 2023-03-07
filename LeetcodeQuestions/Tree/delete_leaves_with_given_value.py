

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #  we need to recursively continue to delete nodes with the target value until we can no longer do so.
        # so we simply have a binary Tree and need to accomplish a couple of tasks
        #  find the target value within the tree
        #  we need to traverse the tree
        #  we can do so using either BFS or DFS or an iterative approach
        #  since this question doesn't deal with the trees levels, bfs is a no
        #  DFS makes the most sense here
        #  this will be a recursive function that will traverse a path within the tree until we have identified the target
        #  a simple template for this traversal looks like this
        #  if node.val == target:
        #  do something

        #  dfs(node.left)
        #  dfs(node.right)
        #  delete that target
        #  since we want to delete all occurrences of that value it might be best if we drill all the way down to the left nodes and then start the deletion process.
        #  If we found a hanging leaf meaning our parent has the target value but it isn't a leaf node yet since it has a child node, then what?
        #  i will make the assumption that the target value will always be in a state that it can be deleted

        #  so if the node is not none then we should continue to search further
        if root:
            #  now we search its left and right sides
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            #  if we finally get to a leaf node then we can delete by return None
            if not root.left and not root.right and root.val == target:
                return None

        #  if the node is None then there is no need to continue looking any further
        return root
