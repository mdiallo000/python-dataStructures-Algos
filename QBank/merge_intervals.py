from curses import keyname


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # test case = [[1,5],[7,8],[12,17],[2,4]]
        #  First we sort the orignal list by the first elem in each sublist
        intervals.sort(key=lambda i: i[0])
        #  now are list is [[1,5],[2,4],[7,8],[12,17]]
        #  now we just want to add the first elem into our array since we will use this to find intervals
        result = [intervals[0]]
        #  result =  [[1,5] ]
        #  now we iterate through our list and determin where there may be intervals
        #  we want to start looking after the first elmen since we are comparing the incoming with the previous
        for start, end in intervals[1:]:
            #  here we take the last elemen from the last entered elem and see wheter
            previous_end = result[-1][1]

            if start <= previous_end:
                result[-1][1] = max(end, previous_end)
            else:
                result.append([start, end])

        return result
