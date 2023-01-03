class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        #  there seems to be no magic bullet to solve this question.
        # For all i know we need to know whether or not a column is sorted or  not
        #  [a,b,c
        #   b,c,e
        #   c,a,e
        remove = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if(strs[j][i] > strs[j+1][i]):
                    remove += 1
                    break
        return remove
