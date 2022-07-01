from curses import keyname


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # test case = [[1,5],[7,8],[12,17],[2,4]]
        #  First we sort the orignal list by the first elem in each sublist
        intervals.sort(key=lambda i: intervals[0][1])
        #  now are list is [[[1,5],[2,4],[7,8],[12,17],]
        #  now we just want to add the first elem into our array since we will use this to find intervals
        result = [intervals[0]]
