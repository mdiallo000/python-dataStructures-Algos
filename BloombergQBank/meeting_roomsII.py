from heapq import heapify


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # # [[0,30],[5,10],[15,20]]
        # start_time = sorted([s.start for s in intervals])
        # # start = [0,5,15]
        # end_time = sorted([s.end for s in intervals])
        # #  end = [10,20,30]

        # nums_rooms = count = 0

        # s = e = 0

        # while s <= len(start_time):

        #     if start_time[s] < end_time[e]:
        #         s += 1
        #         count += 1
        #     else:
        #         e += 1
        #         count -= 1
        #     nums_rooms = max(nums_rooms, count)
        # return nums_rooms
