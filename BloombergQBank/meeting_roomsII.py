from heapq import heapify


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        #     Sort the given meetings by their start time.
        #     Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
        #     For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
        #     If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
        #     If not, then we allocate a new room and add it to the heap.
        #     After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

        # Let us not look at the implementation for this algorithm.

        start_time = sorted([s.start for s in intervals])
        end_time = sorted([s.end for s in intervals])
