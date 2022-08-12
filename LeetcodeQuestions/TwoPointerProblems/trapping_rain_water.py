class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = []
        maxRight = []
        maxH = 0

        for i in range(len(height)):

            maxH = max(maxH, height[i])
            maxLeft.append(maxH)
