class Solution:
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda t: t[1])
        minHeap = []
        currPass = 0

        for numPass, start, end in trips:
