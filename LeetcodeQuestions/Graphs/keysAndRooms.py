class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
