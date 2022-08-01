class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums)

    def makeTree(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        curr_max = max(nums)
        index = nums.index(curr_max)
