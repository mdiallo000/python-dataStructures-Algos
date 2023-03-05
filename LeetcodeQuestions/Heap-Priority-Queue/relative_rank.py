class Solution:
    def findRelativeRank(score):

        # medals =  ["Gold Medal", "Silver Medal"]
        heap = []
        for i in range(len(score)):
            heap.append([-score[i]], i)
