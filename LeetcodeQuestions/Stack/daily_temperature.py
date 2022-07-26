class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, elem in enumerate(temperatures):

            while stack and elem > stack[-1][1]:
                i, e = stack.pop()
                pos = idx - i
                res[i] = pos
            stack.append([idx, elem])
        return res
