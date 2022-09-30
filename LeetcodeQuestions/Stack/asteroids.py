class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = 0

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]
