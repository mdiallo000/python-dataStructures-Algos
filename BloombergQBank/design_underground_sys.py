from collections import defaultdict
from tabnanny import check


class UndergroundSystem:

    def __init__(self):
        checkInReg = defaultdict(list)
        journeyTracker = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInReg[id].append(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # If someone leaves the station than we should erase them from the database to conserve money
        start_station, start_time = self.checkInReg[id].pop()
        end_station = stationName
        end_time = t
        #  we take the out info on where the passanger intially gone on their journey and at what time the started this journey

        self.journeyTracker[(start_station, end_station)
                            ][0] += (end_time - start_time)
        #  we will store information about the length of time it took to get from one station to the other
        self.journeyTracker[(start_station, end_station)][1] += 1
        #  we also keep track of how many trips have been taking between these two stations, this will come in handy when calculation the average time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, all_trips = self.journeyTracker[(
            startStation, endStation)].pop()

        average_time = total_time / all_trips
        return average_time
