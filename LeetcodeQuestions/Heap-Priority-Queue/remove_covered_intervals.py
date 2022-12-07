class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))
        #  the above sort will make sure we not only sort by the smallest start time but also in the case of a tie, we give priotity for the bigger end time time
        #  so a test case like this [[1,4], [1,2], [3,4]]
        res = 0 
        previous =  0
        for _ , end in intervals: 
            
            if end > previous:
                res +=1
                previous = end 
        return res 
        