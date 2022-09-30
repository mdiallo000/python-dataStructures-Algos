class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop
            if a:
                stack.append(a)
        return stack
