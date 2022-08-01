from idna import valid_contextj


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums)

    def makeTree(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        curr_max = max(nums)
        pos = nums.index(curr_max)
        node = TreeNode(curr_max)

        node.left = self.makeTree(nums[:pos])
        node.right = self.makeTree(nums[pos+1:])

        return node
