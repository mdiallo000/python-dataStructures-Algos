from collections import defaultdict
from tabnanny import check


class UndergroundSystem:

    def __init__(self):
        checkInReg = defaultdict(list)
        journeyTracker = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        checkInReg[id].append(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.person

    def getAverageTime(self, startStation: str, endStation: str) -> float:
